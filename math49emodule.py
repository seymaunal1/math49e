from pathlib import Path


def get_files_path() -> Path:
    return Path(__file__).parent / "files"
