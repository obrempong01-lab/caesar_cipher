"""
history.py
----------
Handles saving and reading cipher history.
"""

from datetime import datetime

FILE_NAME = "history.txt"


def save_history(original: str, result: str, shift: int, direction: str) -> None:
    """
    Save a cipher operation to a file.
    """

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, "a") as file:
        file.write(f"{time} | {direction.upper()} | shift={shift} | {original} -> {result}\n")


def read_history() -> str:
    """
    Read the history file.

    Returns:
        str: All saved history or a message if empty.
    """

    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()

            if not content:
                return "No history found."

            return content

    except FileNotFoundError:
        return "No history found."