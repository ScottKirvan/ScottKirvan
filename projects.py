# Add projects here, then run: python scripts/generate_featured.py
PROJECTS = [
    {
        "name": "QuKi Notes",
        "repo": "ScottKirvan/QuKi-Notes",
        "logo": "assets/media/QuKiNotes_v2_Rainbow.svg",
        "logo_width": 120,
        "description": "Cross-platform, zero-friction scratchpad, pasteboard, & blank canvas.",
        "starline": True,
        "links": [
            {"type": "download", "url": "https://github.com/ScottKirvan/QuKi-Notes/releases"},
            {"type": "book-open", "url": "https://scottkirvan.github.io/QuKi-Notes/"},
        ],
        "tag_groups": [
            ["flutter", "markdown"],
            ["android", "windows", "linux"],
        ],
    },
    {
        "name": "BojuBot",
        "repo": "ScottKirvan/BojuBot",
        "logo": "https://raw.githubusercontent.com/ScottKirvan/BojuBot/main/assets/media/BojuBotSprite_800x800.png",
        "logo_width": 120,
        "description": "More than a writing assistant — BojuBot turns your Obsidian vault into a personal AI platform.",
        "starline": True,
        "links": [
            {"type": "download", "url": "https://github.com/ScottKirvan/BojuBot/releases"},
            {"type": "book-open", "url": "https://scottkirvan.github.io/BojuBot/"},
        ],
        "tag_groups": [
            ["typescript", "obsidian", "markdown"],
        ],
    },
]
