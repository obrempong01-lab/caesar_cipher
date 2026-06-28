"""
ui.py
------
Handles all user interface (display only).
"""


def display_banner() -> None:
    print("=" * 50)
    print("🔐        CAESAR CIPHER PROGRAM")
    print("=" * 50)


def display_menu() -> None:
    print(" 🔽 Menu")
    print("\n" + "=" * 50)
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. View History")
    print("4. Exit")
    print("=" * 50)


def display_result(original: str, result: str, shift: int, direction: str) -> None:
    print("\n" + "=" * 50)
    print(f"Original Message : {original}")
    print(f"Shift Key        : {shift}")

    if direction == "encode":
        print(f"Encoded Message  : {result}")
    else:
        print(f"Decoded Message  : {result}")

    print("=" * 50)


def display_history(history: str) -> None:
    print("\n" + "=" * 50)
    print("📜 CIPHER HISTORY")
    print("=" * 50)
    print(history)
    print("=" * 50)


def goodbye() -> None:
    print("\nThank you for using Caesar Cipher!")
    print("Goodbye! 👋")


def get_message() -> str:
    return input("Type your message: ").lower()