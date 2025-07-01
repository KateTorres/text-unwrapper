# Opens last directory to select a file.
# Saves last directory.

import os

LAST_DIR_PATH = "last_dir.txt"

def get_last_directory():
    """Return the last accessed directory if available, else current working directory."""
    if os.path.exists(LAST_DIR_PATH):
        with open(LAST_DIR_PATH, "r", encoding="utf-8") as f:
            return f.read().strip()
    return os.getcwd()

def save_last_directory(path):
    """Save the directory path for future reuse."""
    with open(LAST_DIR_PATH, "w", encoding="utf-8") as f:
        f.write(path)