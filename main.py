from os import makedirs
from pathlib import Path
from shutil import move

from file_extensions import code, design_files, documents, images, music, videos


def categorise_file(file: Path, directory: str) -> None:

    file_extension = file.suffix  # Get the file extension

    if file_extension in images:

        dest_dir = Path(directory) / "Images"

    elif file_extension in videos:

        dest_dir = Path(directory) / "Videos"

    elif file_extension in music:

        dest_dir = Path(directory) / "Music"

    elif file_extension in documents:

        dest_dir = Path(directory) / "Documents"

    elif file_extension in code:

        dest_dir = Path(directory) / "Code"

    elif file_extension in design_files:

        dest_dir = Path(directory) / "Design Files"

    else:

        dest_dir = Path(directory) / "Miscellaneous"

    makedirs(dest_dir, exist_ok=True)  # Create the directory if it doesn't exist
    move(str(file), str(dest_dir / file.name))  # Move the file


def main(directory: Path) -> None:

    for file in directory.iterdir():

        if file.is_dir():

            pass

        else:

            categorise_file(file, str(directory))


if __name__ == "__main__":

    dir_path = input("What is your directory path?: ")
    dir_path = Path(dir_path).expanduser()

    if dir_path.is_dir():

        main(dir_path)

    else:

        print("Invalid input. You must enter a directory.")
