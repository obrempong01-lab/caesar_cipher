"""
validator.py
-------------
Contains all functions for validating user input.
"""


def get_menu_choice() -> int:
    """
    Ask the user to choose a menu option.

    Returns:
        int: 1 (Encode), 2 (Decode), or 3 (Exit)
    """

    while True:
        try:
            choice = int(input("Choose an option: "))

            if choice in (1, 2, 3):
                return choice

            print("❌ Please choose 1, 2 or 3.")

        except ValueError:
            print("❌ Please enter a valid number.")


def get_shift() -> int:
    """
    Prompt the user to enter a valid shift value.

    Returns:
        int: The shift amount.
    """

    while True:
        try:
            return int(input("Enter the shift number: "))
        except ValueError:
            print("❌ Error! Please enter a valid integer.")


def ask_to_continue() -> bool:
    """
    Ask the user whether to continue.

    Returns:
        bool:
            True if the user wants to continue.
            False otherwise.
    """

    while True:
        answer = input("\nDo you want to continue? (yes/no): ").lower()

        if answer == "yes":
            return True

        if answer == "no":
            return False

        print("❌ Error! Please type only 'yes' or 'no'.")