#!/usr/bin/env python3
"""
generate_nav.py

notes/ 폴더 구조를 읽어서 mkdocs.yml 의 nav 섹션을 자동으로 생성/갱신하는 스크립트.

전제:
- docs_dir: "notes"
- Sync_Path 는 이미 Category/Subcategory/... 구조로 생성되고 있음
- front matter 에 최소한 다음 필드가 있음:
    - title: "Vector Spaces"
    - chapter: 1 (optional)
    - section: 1 (optional)
"""

import os
import re
from pathlib import Path

import yaml  # pip install pyyaml

DOCS_DIR = Path("notes")
MKDOCS_YML = Path("mkdocs.yml")


def read_meta(md_path: Path):
    """
    front matter 에서 title, chapter, section 을 읽어온다.
    chapter, section 은 문자열 형태로 반환(라벨용).
    """
    default_title = md_path.stem.replace("_", " ")

    title = None
    chapter = None
    section = None

    try:
        with md_path.open(encoding="utf-8") as f:
            lines = list(f)

        if not lines or not lines[0].strip().startswith("---"):
            return default_title, chapter, section

        # front matter 끝나는 지점 찾기
        end_idx = None
        for i in range(1, len(lines)):
            if lines[i].strip().startswith("---"):
                end_idx = i
                break
        if end_idx is None:
            return default_title, chapter, section

        for line in lines[1:end_idx]:
            s = line.strip()
            if s.startswith("title:"):
                value = s.split(":", 1)[1].strip()
                value = value.strip('"').strip("'")
                if value:
                    title = value
            elif s.startswith("chapter:"):
                value = s.split(":", 1)[1].strip()
                if value:
                    chapter = value
            elif s.startswith("section:"):
                value = s.split(":", 1)[1].strip()
                if value:
                    section = value

    except Exception:
        return default_title, chapter, section

    return title or default_title, chapter, section


def chapter_number_from_name(name: str) -> int:
    """
    chapter_1_vector_spaces.md or chapter_1 → 1
    """
    m = re.match(r"chapter_(\d+)", name)
    return int(m.group(1)) if m else 0


def section_key_from_filename(name: str):
    """
    sec_1_spaces.md → (1,)
    sec_1_1_spaces.md → (1,1)
    정렬용 키.
    """
    m = re.match(r"sec_([0-9_]+)_", name)
    if not m:
        return (9999,)
    parts = m.group(1).split("_")
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (9999,)


def build_subject_nav(subject_dir: Path):
    """
    하나의 Subcategory(예: Linear_Algebra) 안에서 nav 구조를 만든다.

    반환 형식 예:
    [
      {"Introduction to Linear Algebra": "Mathematics/Linear_Algebra/intro.md"},
      {
        "Chapter 1": [
          {"1 Vector Spaces": "..."},
          {"1.1 Vector Spaces and Subspaces": "..."},
        ]
      }
    ]
    """
    items = []

    def rel(path: Path) -> str:
        return str(path.relative_to(DOCS_DIR)).replace("\\", "/")

    # 1) subject 루트의 md 파일들
    md_files = sorted(
        [p for p in subject_dir.glob("*.md") if p.is_file()],
        key=lambda p: p.name,
    )

    subject_intro_items = []
    chapter_intro_map = {}  # ch_num -> (title, rel_path)

    for md in md_files:
        name = md.name
        t, ch, sec = read_meta(md)

        if name.startswith("chapter_"):
            ch_num = chapter_number_from_name(name)
            chapter_intro_map[ch_num] = (t, rel(md))
        else:
            # 과목 인트로/기타
            subject_intro_items.append({t: rel(md)})

    # 2) chapter_* 폴더들
    chapter_dirs = sorted(
        [d for d in subject_dir.glob("chapter_*") if d.is_dir()],
        key=lambda d: chapter_number_from_name(d.name),
    )

    chapter_items = []

    for ch_dir in chapter_dirs:
        ch_num = chapter_number_from_name(ch_dir.name)

        ch_intro_title, ch_intro_path = None, None
        if ch_num in chapter_intro_map:
            ch_intro_title, ch_intro_path = chapter_intro_map[ch_num]

        # 섹션 파일들 정렬
        sections = sorted(
            [p for p in ch_dir.glob("*.md") if p.is_file()],
            key=lambda p: section_key_from_filename(p.name),
        )

        section_nav = []

        # 챕터 인트로
        if ch_intro_title and ch_intro_path:
            label = f"{ch_num} {ch_intro_title}"
            section_nav.append({label: ch_intro_path})

        # 일반 섹션들
        for sec in sections:
            t, ch_meta, sec_meta = read_meta(sec)

            # 번호 prefix 만들기: chapter.section
            prefix = ""
            if sec_meta:
                # 섹션 번호는 그대로 문자열로 사용 (예: "1", "1.1")
                prefix = f"{ch_num}.{sec_meta} "

            label = f"{prefix}{t}" if prefix else t
            section_nav.append({label: rel(sec)})

        if not section_nav:
            continue

        chapter_label = f"Chapter {ch_num}"
        chapter_items.append({chapter_label: section_nav})

    items.extend(subject_intro_items)
    items.extend(chapter_items)
    return items


def build_nav():
    """
    전체 nav 구조 생성.

    nav:
      - Deep Notes:
          - Mathematics:
              - Linear_Algebra:
                  ...
    """
    nav_root = []

    if not DOCS_DIR.exists():
        raise SystemExit(f"{DOCS_DIR} does not exist")

    for category_dir in sorted(DOCS_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        category_label = category_dir.name
        subjects = []

        for subject_dir in sorted(category_dir.iterdir()):
            if not subject_dir.is_dir():
                continue
            subject_label = subject_dir.name
            subject_nav = build_subject_nav(subject_dir)
            subjects.append({subject_label: subject_nav})

        if subjects:
            nav_root.append({category_label: subjects})

    return [{"Deep Notes": nav_root}]


def update_mkdocs_nav():
    """mkdocs.yml 파일의 nav 섹션을 갱신한다."""
    if not MKDOCS_YML.exists():
        raise SystemExit("mkdocs.yml not found")

    with MKDOCS_YML.open(encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config["nav"] = build_nav()

    with MKDOCS_YML.open("w", encoding="utf-8") as f:
        yaml.dump(config, f, sort_keys=False, allow_unicode=True)

    print("Updated mkdocs.yml 'nav' section successfully.")


if __name__ == "__main__":
    update_mkdocs_nav()
