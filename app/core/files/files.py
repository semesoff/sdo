import os
from pathlib import Path


def save_file(directory_path: str, file_name: str, file_content: bytes) -> str:
    Path(directory_path).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(file_content)
    return file_path


def delete_file(file_path: str) -> bool:
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError:
        return False
    except Exception as error:
        return False