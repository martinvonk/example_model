from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def get_all_files(root: Path) -> list[Path]:
    """Returns a list of all files in the repository root, excluding hidden files and directories."""
    files = [
        f.relative_to(root)
        for f in root.rglob("*")
        if f.is_file()
        and not any(part.startswith(".") for part in f.relative_to(root).parts)
    ]
    return files


def check_file_extensions(files: list[Path]) -> list[Path]:
    """Returns a list of files whose extensions are in the allowed set."""

    allowed_extensions = (
        "md",
        "py",
        "yml",
        "yaml",
        "json",
        "gitignore",
        "ini",
        "cfg",
        "toml",
        "ipynb",
        "lock",
        "",
    )
    disallowed_files = []
    for file in files:
        ext = file.suffix.lower().strip(".")
        if ext not in allowed_extensions:
            disallowed_files.append(file)
    return disallowed_files


def check_file_sizes(files: list[Path]) -> list[Path]:
    """Return files larger than 5 MB from the given list."""
    maximum_filesize: int = 5242880  # 5 MB
    disallowed_files = []
    for file in files:
        size = file.stat().st_size
        if size > maximum_filesize:
            disallowed_files.append(file)
    return disallowed_files


if __name__ == "__main__":
    files = get_all_files(REPO_ROOT)
    extensions = check_file_extensions(files)
    if extensions:
        raise ValueError(f"Files with illegal extensions found: {extensions}")

    sizes = check_file_sizes(files)
    if sizes:
        raise ValueError(f"Files exceeding maximum size (5MB) found: {sizes}")
