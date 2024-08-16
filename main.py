from pathlib import Path


def organise_dir(path: str):
    pass


if __name__ == "__main__":

    dir_path = input("What is your directory path?: ")
    dir_path = Path(dir_path).expanduser()

    if dir_path.is_dir():
        organise_dir(dir_path)
    else:
        print("Invalid input. You must enter a directory.")
