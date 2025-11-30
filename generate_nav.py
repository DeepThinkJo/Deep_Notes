#!/usr/bin/env python3
"""
generate_nav.py

notes/ 폴더 구조를 읽어서 mkdocs.yml 의 nav 섹션을 자동으로 생성/갱신하는 스크립트.

전제:
- docs_dir: "notes"
- Sync_Path 는 이미 Category/Subcategory/... 구조로 생성되고 있음
- 파일의 front matter 에 title: "..." 이 들어 있음 (sync_notion.py 가 작성)

설정:
- 카테고리 = notes/ 아래 1단계 폴더 이름 (예: Mathematics)
- 서브카테고리 = 그 안의 2단계 폴더 이름 (예: Linear Algebra)
- 챕터 인트로 파일: 이름이 chapter_로 시작하는 .md
- 챕터 섹션 파일: notes/Category/Subcategory/chapter_N/sec_*_slug.md
"""

import os
import re
from pathlib import Path

import yaml  # pip install pyyaml

DOCS_DIR = Path("notes")
MKDOCS_YML = Path("mkdocs.yml")


def read_title(md_path: Path) -> str:
    """Markdown 파일의 front matter 에서 title 값을 읽어옴."""
    try:
        with md_path.open(encoding="utf-8") as f:
            lines = list(f)

        if not lines or not lines[0].strip().startswith("---"):
            # front matter 없음 → 파일명으로 대체
            return md_path.stem.replace("_", " ")

        # front matter 범위 찾기
        for i in range(1, len(lines)):
            if lines[i].strip().startswith("---"):
                end_idx = i
                break
        else:
            end_idx = 0

        # front matter 안에서 title: 찾기
        for line in lines[1:end_idx]:
            if line.strip().startswith("title:"):
                # title: "...."
                _, value = line.split(":", 1)
                value = value.strip().strip('"').strip("'")
                return value or md_path.stem.replace("_", " ")
    except Exception:
        pass

    return md_path.stem.replace("_", " ")


def chapter_number_from_name(name: str) -> int:
    """
    chapter_1_vector_spaces.md → 1
    chapter_2 → 2
    chapter_1_1_... (혹시라도) → 1
    """
    m = re.match(r"chapter_(\d+)", name)
    return int(m.group(1)) if m else 0


def section_key_from_filename(name: str):
    """
    sec_1_spaces.md → (1,)
    sec_1_1_spaces.md → (1,1)
    이런 tuple 로 만들어서 정렬에 사용.
    """
    m = re.match(r"sec_([0-9_]+)_", name)
    if not m:
        return (9999,)  # 정렬상 맨 뒤로
    parts = m.group(1).split("_")
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (9999,)


def build_subject_nav(subject_dir: Path):
    """
    하나의 Subcategory(예: Linear Algebra) 안에서 nav 구조를 만든다.
    반환 형식: [ { "Page title": "Relative/Path.md" }, { "Chapter 1: ...": [...] }, ... ]
    """
    items = []

    # 상대 경로는 docs_dir 기준
    def rel(path: Path) -> str:
        return str(path.relative_to(DOCS_DIR)).replace("\\", "/")

    # 1) subject 루트에 있는 md 파일들
    md_files = sorted(
        [p for p in subject_dir.glob("*.md") if p.is_file()],
        key=lambda p: p.name,
    )

    subject_intro_items = []
    chapter_intro_map = {}  # chapter_num -> (title, path)

    for md in md_files:
        name = md.name
        if name.startswith("chapter_"):
            ch = chapter_number_from_name(name)
            chapter_intro_map[ch] = (read_title(md), rel(md))
        else:
            # 일반 intro / 기타 페이지
            subject_intro_items.append({read_title(md): rel(md)})

    # 2) chapter_N 폴더들
    chapter_dirs = sorted(
        [d for d in subject_dir.glob("chapter_*") if d.is_dir()],
        key=lambda d: chapter_number_from_name(d.name),
    )

    chapter_items = []

    for ch_dir in chapter_dirs:
        ch_num = chapter_number_from_name(ch_dir.name)

        # 챕터 인트로가 있다면 먼저 사용, 없으면 폴더 이름 사용
        ch_intro_title, ch_intro_path = None, None
        if ch_num in chapter_intro_map:
            ch_intro_title, ch_intro_path = chapter_intro_map[ch_num]

        sections = sorted(
            [p for p in ch_dir.glob("*.md") if p.is_file()],
            key=lambda p: section_key_from_filename(p.name),
        )

        section_nav = []
        if ch_intro_title and ch_intro_path:
            # 챕터 자체도 클릭 가능한 페이지로 추가해주고 싶으면 여기서 추가
            section_nav.append({ch_intro_title: ch_intro_path})

        for sec in sections:
            section_nav.append({read_title(sec): rel(sec)})

        if not section_nav:
            continue

        chapter_label = f"Chapter {ch_num}"
        chapter_items.append({chapter_label: section_nav})

    # 3) 최종 subject nav = intro 페이지들 + 챕터들
    items.extend(subject_intro_items)
    items.extend(chapter_items)
    return items


def build_nav():
    """
    전체 nav 구조를 생성해서 Python 객체로 반환.
    형식:
    nav:
      - Deep Notes:
          - Mathematics:
              - Linear Algebra:
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

    # 최상위에서 "Deep Notes" 라는 루트 메뉴를 하나 만든다.
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
