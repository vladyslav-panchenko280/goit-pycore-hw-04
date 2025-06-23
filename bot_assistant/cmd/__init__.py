from .hello import hello_command
from .close import close_command
from  .invalid import invalid_command
from .add import add_contact
from .change import change_contact
from .phone import show_contact
from .all import show_all

class Command:
    HELLO = "hello"
    CLOSE = "close"
    EXIT = "exit"
    ADD = "add"
    INVALID = "invalid"
    CHANGE = "change"
    FIND = "find"
    ALL = "all"

COMMAND_HANDLERS = {
    Command.HELLO: hello_command,
    Command.CLOSE: close_command,
    Command.EXIT: close_command,
    Command.ADD: add_contact,
    Command.INVALID: invalid_command,
    Command.CHANGE: change_contact,
    Command.FIND: show_contact,
    Command.ALL: show_all,
}

__all__ = ["COMMAND_HANDLERS", "Command"]