import pathlib
import os

def get_db_path() -> str:
    home_directory: pathlib.Path = pathlib.Path.home()
    directory_path: str = os.path.join(home_directory, '.expensy')
    try:
        os.mkdir(directory_path)
    except FileExistsError:
        pass
    return os.path.join(directory_path, 'expenses.db')