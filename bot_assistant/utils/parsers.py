def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = user_input.split()
    return cmd, args