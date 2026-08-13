# !/usr/bin/env python3
"""Generates the featured-projects HTML block from projects.py.

Usage: python scripts/generate_featured.py
Output: featured_projects.md  (copy-paste into README.md where you want it)
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from projects import PROJECTS

ICON_FILE_MAP = {
    "microsoft": "microsoft-svgrepo-com",
}

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

    links_html = "".join(icon_pair_html(
        lnk["type"], url=lnk["url"]) for lnk in links)

    groups_html = SEPARATOR.join(
        "".join(icon_pair_html(
            tag, url=f"https://github.com/topics/{tag}") for tag in group)
        for group in tag_groups
    )

    if links_html and groups_html:
        bottom = links_html + SEPARATOR + groups_html
    else:
        bottom = links_html or groups_html

    return f"{logo}{title}\n{description}<br>\n{bottom}"


def generate(projects):
    heading = "# Featured Projects:" if len(
        projects) != 1 else "# Featured Project:"
    lines = [heading, ""]
    for p in projects:
        lines.append(render_project(p))
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(os.path.dirname(
        script_dir), "featured_projects.md")

    block = generate(PROJECTS)

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(block)

    print(f"Written to {out_path}")
    print()
    print(block)
