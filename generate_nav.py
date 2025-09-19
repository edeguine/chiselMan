#!/usr/bin/env python3
import os
import re
from pathlib import Path

# ====== EDIT THIS ORDER ======
folders_in_order = ['workflow', 'brushes',  'materials', 'layers','prefs', 'misc', 'beta', 'licenses']
# =============================

DOCS_DIR = Path('docs')
IGNORE_FOLDERS = {'img', 'stylesheets', '.git', '.github', '__pycache__'}

def natural_key(s: str):
    # Split into digit and non-digit chunks: "10_file.md" > ["", 10, "_file.md"]
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]

def list_md_files(folder: Path):
    # Only direct children, only .md files
    files = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == '.md']
    # Sort by natural order of filename (so 2_... comes after 10_... correctly)
    files.sort(key=lambda p: natural_key(p.name))
    return files

def header_from_folder(name: str):
    # “capitalize first letter”, keep the rest as-is
    return name[:1].upper() + name[1:]

def discover_ordered_folders():
    existing = {p.name for p in DOCS_DIR.iterdir() if p.is_dir()}
    # keep only those that exist and aren’t ignored
    ordered = [f for f in folders_in_order if f in existing and f not in IGNORE_FOLDERS]
    # append any remaining folders (not listed) alphabetically
    remaining = sorted([f for f in existing if f not in set(ordered) and f not in IGNORE_FOLDERS])
    return ordered + remaining

def generate_nav_yaml():
    lines = []
    lines.append("nav:")
    # Optional: include Home first if docs/index.md exists
    index_md = DOCS_DIR / "index.md"
    if index_md.exists():
        lines.append(f"  - Home: index.md")

    for folder_name in discover_ordered_folders():
        folder_path = DOCS_DIR / folder_name
        md_files = list_md_files(folder_path)
        if not md_files:
            continue

        # section header
        lines.append(f"  - {header_from_folder(folder_name)}:")
        for f in md_files:
            # skip files starting with '.' (hidden) just in case
            if f.name.startswith('.'):
                continue
            # Only two levels: docs/top/<file>.md
            rel_path = f"{folder_name}/{f.name}"
            lines.append(f"      - {rel_path}")

    return "\n".join(lines)

if __name__ == "__main__":
    if not DOCS_DIR.exists():
        raise SystemExit("Error: run this script from the repo root (parent of 'docs/').")
    print(generate_nav_yaml())
