from utils import *
from handlers import *
from colorama import Fore
import sys

def visualise_dir_structure() -> None:
    try:
        path = validate_args(sys.argv)
    except ValueError as e:
        colorful_print(f"{e}", Fore.RED)
        sys.exit(1)

    print_folder_tree(path)

if __name__ == "__main__":
    visualise_dir_structure()
