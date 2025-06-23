from pathlib import Path
from colorama import Fore, Style
from utils.colorful_print import colorful_print

def print_folder_tree(path: str, level: int = 0) -> None:
    
    path = Path(path)

    if not path.exists():
        colorful_print(f"Error: path does not exist.", Fore.RED)
        return

    if not path.is_dir():
        colorful_print(f"Error: path is not a directory.", Fore.RED)
        return

    indent = " " * (level * 4)
    colorful_print(f"{indent}{path.name}/", Fore.BLUE)

    for item in path.iterdir():
        if item.is_dir():
            print_folder_tree(item, level + 1)
        else:
            colorful_print(f"{indent}    {item.name}", Fore.GREEN)