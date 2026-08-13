#!/usr/bin/env python3
"""Regenerates the Featured Projects block in README.md from projects.py.

Usage: python scripts/generate_featured.py [--dry-run]
"""

import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from projects import PROJECTS

# Maps tag/type name → icon filename stem (when it differs from the tag name)
ICON_FILE_MAP = {
    "microsoft": "microsoft-svgrepo-com",
}

# Maps tag/type name → display name for alt text
DISPLAY_NAMES = {
    "cplusplus": "C++",
    "gnubash": "Bash",
    "unrealengine": "Unreal Engine",
    "typescript": "TypeScript",
    "githubsponsors": "GitHub Sponsors",
    "kofi": "Ko-fi",
    "square-terminal": "Terminal",
    "book-open": "Docs",
    "microsoft": "Windows",
}

SEPARATOR = "&nbsp;&nbsp;&nbsp;&bull;&nbsp;"
ICON_HEIGHT = 20


def icon_file(tag):
    return ICON_FILE_MAP.get(tag, tag)


def display_name(tag):
    return DISPLAY_NAMES.get(tag, tag.replace("-", " ").title())


def icon_pair_html(tag, url=None):
    stem = icon_file(tag)
    alt = display_name(tag)
    imgs = (
        f'<img src="assets/media/{stem}-light.svg#gh-light-mode-only" alt="{alt}" height="{ICON_HEIGHT}" border="1" />'
        f'<img src="assets/media/{stem}-dark.svg#gh-dark-mode-only" alt="{alt}" height="{ICON_HEIGHT}" border="1" />'
    )
    if url:
        return f'<a href="{url}">{imgs}</a>'
    return imgs


def starline_html(repo):
    return (
        f'<img src="https://raw.githubusercontent.com/{repo}/refs/heads/starlines/{repo}/starline.svg"'
        f' alt="starline" height="36"/>'
    )


def render_project(p):
    logo_src = p["logo"]
    logo_width = p.get("logo_width", 120)
    name = p["name"]
    repo = p["repo"]
    description = p["description"]
    has_starline = p.get("starline", False)
    links = p.get("links", [])
    tag_groups = p.get("tag_groups", [])

    logo = f'<img src="{logo_src}" width="{logo_width}" align="left" border="0" />'

    title_inner = name
    if has_starline:
        title_inner += starline_html(repo)
    title = f'<h3><a href="https://github.com/{repo}">{title_inner}</a></h3>'

    links_html = "".join(icon_pair_html(lnk["type"], url=lnk["url"]) for lnk in links)

    groups_html = SEPARATOR.join(
        "".join(icon_pair_html(tag, url=f"https://github.com/topics/{tag}") for tag in group)
        for group in tag_groups
    )

    if links_html and groups_html:
        bottom = links_html + SEPARATOR + groups_html
    else:
        bottom = links_html or groups_html

    return f"{logo}{title}\n{description}<br>\n{bottom}"


def generate_block(projects):
    heading = "# Featured Projects:" if len(projects) != 1 else "# Featured Project:"
    sections = [f"\n{heading}\n"]
    for p in projects:
        sections.append("\n" + render_project(p) + "\n\n---\n")
    return (
        "<!-- Begin Featured Projects -->\n"
        + "".join(sections)
        + "\n<!-- End Featured Projects -->"
    )


def update_readme(readme_path, block, dry_run=False):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"<!-- Begin Featured Projects -->.*?<!-- End Featured Projects -->"
    new_content, count = re.subn(pattern, block, content, flags=re.DOTALL)

    if count == 0:
        print(
            "WARNING: <!-- Begin Featured Projects --> marker not found in README.md.\n"
            "Add the markers around the featured section, then re-run."
        )
        return False

    if dry_run:
        print("--- DRY RUN: would write the following block ---")
        print(block)
        return True

    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)
    print(f"README.md updated ({count} block replaced).")
    return True


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(os.path.dirname(script_dir), "README.md")

    block = generate_block(PROJECTS)
    update_readme(readme_path, block, dry_run=dry_run)
