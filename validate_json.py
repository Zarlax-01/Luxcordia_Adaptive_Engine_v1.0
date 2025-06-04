#!/usr/bin/env python3
"""Simple JSON validator for project files."""
import json
import sys
import glob


def validate(path: str) -> None:
    """Load JSON file to ensure it is syntactically correct."""
    with open(path, 'r', encoding='utf-8') as f:
        json.load(f)


def main(paths):
    for path in paths:
        try:
            validate(path)
            print(f"{path}: OK")
        except Exception as exc:
            print(f"{path}: ERROR {exc}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = glob.glob('*.json')
    main(files)
