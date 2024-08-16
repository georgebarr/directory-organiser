# Directory Organiser Script

## Overview

This Python script categorises files in a given directory based on their file type. The script automatically sorts files into specific folders such as **Images**, **Documents**, **Miscellaneous**, **Videos**, **Code**, **Design Files**, and **Music**. The organisation process only affects files that are not already contained within a folder.

## Supported File Types

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg`, `.tiff`, `.bmp`, `.webp`
- **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, `.wmv`, `.webm`
- **Music**: `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`
- **Documents**: `.pdf`, `.docx`, `.doc`, `.xlsx`, `.xls`, `.txt`, `.rtf`
- **Design Files**: `.psd`, `.ai`, `.indd`, `.sketch`, `.blend`, `.obj`, `.fbx`
- **Code**: `.py`, `.c`, `.js`, `.css`, `.html`, `.java`, `.xml`, `.cpp`, `.json`
- **Miscellaneous**: Files that do not match the above categories will be moved to a `Miscellaneous` folder.

## How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/georgebarr/directory-organiser.git
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd directory-organiser
    ```

3. **Run the script**:
    ```bash
    python main.py
    ```

4. **Input the path of the directory you wish to organise**:
    ```
    What is your directory path?:  $
    ```

6. **Check the organised files**:
    - Check the specified directory. You will find new folders like **Images**, **Documents**, **Videos**, **Code**, **Design Files**, **Music**, and **Miscellaneous**, with the respective files sorted into them.

## Licence

This project is licensed under the MIT Licence. See the [LICENCE](https://github.com/georgebarr/directory-organiser/blob/main/LICENSE) file for more details.

---

Feel free to contribute, report issues, or fork this project to tailor it to your needs. Happy organising!
