import yaml
from pathlib import Path

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
    nav 에서는 홈(index.md)은 제외한다.
    """
    pages = []

    for md_path in NOTES_DIR.rglob("*.md"):
        # 홈 페이지(index.md)는 nav 에서 제외
        if md_path.name == "index.md" and md_path.parent == NOTES_DIR:
            continue

        meta = parse_front_matter(md_path)

        title = meta.get("title") or md_path.stem
        category = meta.get("category") or "Misc"
        subcategory = meta.get("subcategory") or "General"
        chapter = meta.get("chapter")
        section = meta.get("section")

        # docs_dir 가 notes 이므로, nav 경로는 notes/ 기준 상대 경로여야 한다.
        rel_path = md_path.relative_to(NOTES_DIR).as_posix()

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
    구조:
      - Deep Notes:
          - Category:
              - Subcategory:
                  - Chapter X – Title:
                      - Title: path          (챕터 메인)
                      - X.Y Subtitle: path   (섹션들)
    """
    # category / subcategory / chapter 기준으로 트리 구성
    tree = {}

    for p in pages:
        cat = p["category"]
        sub = p["subcategory"]
        ch = p["chapter"]

        tree.setdefault(cat, {}).setdefault(sub, {}).setdefault(ch, []).append(p)

    deep_notes_children = []

    # 카테고리 정렬
    for cat in sorted(tree.keys()):
        sub_dict = tree[cat]
        sub_entries = []

        # 서브카테고리 정렬
        for sub in sorted(sub_dict.keys()):
            chapter_dict = sub_dict[sub]
            chapter_entries = []

            # chapter 정렬 (None 은 맨 뒤로)
            def chapter_sort_key(ch_key):
                return (9999 if ch_key is None else ch_key)

            for ch in sorted(chapter_dict.keys(), key=chapter_sort_key):
                items = chapter_dict[ch]

                # chapter 정보가 없는 페이지들은 서브카테고리 바로 아래에 나열
                if ch is None:
                    # section 기준 정렬
                    items.sort(
                        key=lambda item: (
                            9999 if item["section"] is None else item["section"],
                            item["title"],
                        )
                    )
                    for item in items:
                        chapter_entries.append({item["title"]: item["path"]})
                    continue

                # chapter 가 있는 경우: main 과 섹션 구분
                main_page = None
                sections = []

                for item in items:
                    if item["section"] is None and main_page is None:
                        main_page = item
                    else:
                        sections.append(item)

                # 섹션 정렬
                sections.sort(
                    key=lambda item: (
                        9999 if item["section"] is None else item["section"],
                        item["title"],
                    )
                )

                # 챕터 제목 결정
                if main_page:
                    base_title = main_page["title"]
                else:
                    base_title = f"Chapter {ch}"

                chapter_label = f"Chapter {ch} – {base_title}"

                chapter_children = []

                # 챕터 메인 페이지를 가장 위에 배치
                if main_page:
                    chapter_children.append({base_title: main_page["path"]})

                # 각 섹션에 번호 붙여서 추가
                for sec_item in sections:
                    sec = sec_item["section"]
                    if sec is not None:
                        sec_label = f"{ch}.{sec} {sec_item['title']}"
                    else:
                        sec_label = sec_item["title"]
                    chapter_children.append({sec_label: sec_item["path"]})

                chapter_entries.append({chapter_label: chapter_children})

            sub_entries.append({sub: chapter_entries})

        deep_notes_children.append({cat: sub_entries})

    nav = [
        {"← Back to DeepThinkJo": "https://deepthinkjo.github.io"},
        {"Deep Notes": deep_notes_children}
    ]
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
