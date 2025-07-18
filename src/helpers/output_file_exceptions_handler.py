from colorama import Fore
import os
import pathlib

from .output_file_exceptions import NoDesiredExtention, FileAlreadyExists, FileDirectoryDoesNotExist

def output_file_exception_handler(output_file: str) -> None:
    output_file_directory: str = os.path.dirname(output_file)
    output_file_extention: str = pathlib.Path(output_file).suffix
    
    if os.path.exists(output_file) is True:
        raise FileAlreadyExists(Fore.RED + f"the output file given at {output_file} already exists and can't be overwritten")
    elif os.path.exists(output_file_directory) is False:
        raise FileDirectoryDoesNotExist(Fore.RED + f"the output file given {output_file} doesn't have a valid parent directory")
    elif output_file_extention != '.csv':
        raise NoDesiredExtention(Fore.RED + f"expected .csv as an extention got {output_file_extention}")