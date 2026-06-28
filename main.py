from cipher import caesar_cipher
from validator import get_menu_choice, get_shift, ask_to_continue
from ui import (
    display_banner,
    display_menu,
    display_result,
    display_history,
    goodbye,
    get_message
)
from history import save_history, read_history


# Start program
display_banner()

while True:

    display_menu()
    choice = get_menu_choice()

    # ENCODE
    if choice == 1:
        direction = "encode"

        shift = get_shift()
        text = get_message()

        result = caesar_cipher(text, shift, direction)

        display_result(text, result, shift, direction)

        save_history(text, result, shift, direction)

    # DECODE
    elif choice == 2:
        direction = "decode"

        shift = get_shift()
        text = get_message()

        result = caesar_cipher(text, shift, direction)

        display_result(text, result, shift, direction)

        save_history(text, result, shift, direction)

    # VIEW HISTORY
    elif choice == 3:
        history = read_history()
        display_history(history)

    # EXIT
    else:
        goodbye()
        break

    # Ask to continue (optional safety exit)
    if not ask_to_continue():
        goodbye()
        break