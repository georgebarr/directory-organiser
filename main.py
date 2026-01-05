from os import makedirs
from pathlib import Path
from shutil import move


def categorise_file(file: Path, directory: str) -> None:
    extension_mapping = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".tiff", ".bmp", ".webp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", "flv", ".wmv", ".webm"],
        "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".txt", ".rtf"],
        "Code": [".py", ".c", ".js", ".css", ".html", ".java", ".xml", ".cpp", ".json"],
        "Design Files": [".psd", ".ai", ".indd", ".sketch", ".blend", ".obj", ".fbx"],
    }

    dest_dir = Path(directory) / "Miscellaneous" # Default directory folder if there is no match found

    for folder, extensions in extension_mapping.items():
        if file.suffix.lower() in extensions:
            dest_dir = Path(directory) / folder
            break

    makedirs(dest_dir, exist_ok=True)  # Create the directory if it doesn't exist

    unique_file_path = dest_dir / file.name
    count = 1

    while unique_file_path.exists():
        unique_file_path = dest_dir / f"{file.stem}_{count}{file.suffix}" # Adds an incrementing counter to the file name
        count += 1

    move(str(file), str(unique_file_path))


def main(directory: Path) -> None:
    for file in directory.iterdir():
        if file.is_file():
            categorise_file(file, str(directory))

    print(f"Successful. {directory} has now been organised.")


if __name__ == "__main__":
    dir_path = input("What is your directory path?: ")
    dir_path = Path(dir_path).expanduser()

    if dir_path.is_dir():
        main(dir_path)
    else:
        print(f"{dir_path} is not an existing directory.")
