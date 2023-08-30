import os
import pathlib

SRC_DIR = pathlib.Path(__file__).parent
PROJECT_DIR = SRC_DIR.parent
OUTPUT_DIR = PROJECT_DIR / "out"

if not OUTPUT_DIR.exists():
    os.mkdir(OUTPUT_DIR)
