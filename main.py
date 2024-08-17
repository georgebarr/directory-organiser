from os import makedirs
from pathlib import Path
from shutil import move

from file_extensions import code, design_files, documents, images, music, videos


def categorise_file(file: Path, directory: str) -> None:

    extension_mapping = {
        "Images": images,
        "Videos": videos,
        "Music": music,
        "Documents": documents,
        "Code": code,
        "Design Files": design_files,
    }

    # Default directory folder if there is no match found
    dest_dir = Path(directory) / "Miscellaneous"

    for folder, extensions in extension_mapping.items():

        if file.suffix.lower() in extensions:

            dest_dir = Path(directory) / folder
            break

    if file.name in dest_dir:
        pass

    makedirs(dest_dir, exist_ok=True)  # Create the directory if it doesn't exist
    move(str(file), str(dest_dir / file.name))  # Move the file


def main(directory: Path) -> None:

    for file in directory.iterdir():

        if file.is_file():

            categorise_file(file, str(directory))


if __name__ == "__main__":

    dir_path = input("What is your directory path?: ")
    dir_path = Path(dir_path).expanduser()

    if dir_path.is_dir():

        main(dir_path)

    else:

        print("Invalid input. You must enter the path to an existing directory.")
