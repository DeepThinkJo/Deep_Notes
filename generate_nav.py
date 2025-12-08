import re
from pathlib import Path

import yaml

MKDOCS_PATH = Path("mkdocs.yml")
NOTES_DIR = Path("notes")


def load_mkdocs_config():
    if not MKDOCS_PATH.exists():
        raise SystemExit("mkdocs.yml not found")

    with MKDOCS_PATH.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    return config


def parse_front_matter(md_path: Path) -> dict:
    """
    각 Markdown 파일에서 YAML front matter 부분만 파싱해서 dict로 반환.
    front matter가 없으면 빈 dict 반환.
    """
    text = md_path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        return {}

    # 처음 두 개의 '---' 사이를 front matter 로 간주
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}

    fm_text = parts[1]
    try:
        data = yaml.safe_load(fm_text) or {}
    except Exception:
        data = {}

    return data


def collect_pages():
    """
    notes/ 이하의 모든 .md 파일에 대해
    front matter 정보를 모아서 리스트로 반환.
    """
    pages = []

    for md_path in NOTES_DIR.rglob("*.md"):
        meta = parse_front_matter(md_path)

        title = meta.get("title") or md_path.stem
        category = meta.get("category") or "Misc"
        subcategory = meta.get("subcategory") or "General"
        chapter = meta.get("chapter")
        section = meta.get("section")

        rel_path = md_path.as_posix()  # mkdocs.yml 에서 쓸 경로

        pages.append(
            {
                "title": title,
                "category": category,
                "subcategory": subcategory,
                "chapter": chapter,
                "section": section,
                "path": rel_path,
            }
        )

    return pages


def build_nav_structure(pages):
    """
    pages 리스트를 기반으로 mkdocs nav 구조(list of dicts)를 생성.
    최종 구조:
    nav:
      - Deep Notes:
          - Category:
              - Subcategory:
                  - Title: path
    """
    # category / subcategory 기준으로 그룹화
    tree = {}

    for p in pages:
        cat = p["category"]
        sub = p["subcategory"]

        tree.setdefault(cat, {}).setdefault(sub, []).append(p)

    deep_notes_children = []

    # category 정렬 (알파벳)
    for cat in sorted(tree.keys()):
        sub_dict = tree[cat]
        sub_entries = []

        # subcategory 정렬 (알파벳)
        for sub in sorted(sub_dict.keys()):
            items = sub_dict[sub]

            # chapter, section, title 기준으로 정렬
            def sort_key(item):
                ch = item["chapter"]
                sec = item["section"]

                # chapter / section 이 None 인 경우는 뒤쪽으로 보내기 위해 큰 값 사용
                ch_key = ch if ch is not None else 9999
                sec_key = sec if sec is not None else 9999
                return (ch_key, sec_key, item["title"])

            items.sort(key=sort_key)

            pages_nav = [{item["title"]: item["path"]} for item in items]
            sub_entries.append({sub: pages_nav})

        deep_notes_children.append({cat: sub_entries})

    # 최종 nav 구조
    nav = [{"Deep Notes": deep_notes_children}]
    return nav


def update_mkdocs_nav():
    config = load_mkdocs_config()
    pages = collect_pages()

    if not pages:
        print("No markdown pages found under 'notes/'. nav will be empty.")
        config["nav"] = []
    else:
        nav = build_nav_structure(pages)
        config["nav"] = nav

    with MKDOCS_PATH.open("w", encoding="utf-8") as f:
        # sort_keys=False 로 해서 기존 key 순서를 최대한 유지
        yaml.safe_dump(
            config,
            f,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
        )

    print("mkdocs.yml nav updated.")


if __name__ == "__main__":
    update_mkdocs_nav()
