from colorama import Style

def colorful_print(text: str, color: str) -> None:
    print(f"{color}{text}{Style.RESET_ALL}")