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

    makedirs(dest_dir, exist_ok=True)  # Create the directory if it doesn't exist

    unique_file_path = dest_dir / file.name
    count = 1

    # Check if the file with the same name already exists
    while unique_file_path.exists():

        # Create a new file name by appending an incrementing counter
        unique_file_path = dest_dir / f"{file.stem}_{count}{file.suffix}"

        count += 1

    move(str(file), str(unique_file_path))  # Move the file to the unique file path


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
