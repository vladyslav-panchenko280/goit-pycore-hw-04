from utils import *
from cmd import COMMAND_HANDLERS, Command
import sys

def start_bot() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = sanitize_input(input("Enter a command: "))

        command, args = parse_input(user_input)

        if command in [Command.CLOSE, Command.EXIT]:
            result = COMMAND_HANDLERS[Command.CLOSE]()
            print(result)
            break
        elif command == Command.HELLO:
            result = COMMAND_HANDLERS[Command.HELLO]()
            print(result)
        elif command == Command.CHANGE:
            result = COMMAND_HANDLERS[Command.CHANGE](args, contacts)
            print(result)
        elif command == Command.ADD:
            result = COMMAND_HANDLERS[Command.ADD](args, contacts)
            print(result)
        elif command == Command.FIND:
            result = COMMAND_HANDLERS[Command.FIND](args, contacts)
            print(result)
        elif command == Command.ALL:
            result = COMMAND_HANDLERS[Command.ALL](contacts)
            print(result)
        else:
            result = COMMAND_HANDLERS[Command.INVALID]()
            print(result)

    sys.exit(0)

if __name__ == "__main__":
    start_bot()
