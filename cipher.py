"""
cipher.py
Contains the Caesar Cipher algorithm.
"""

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")


def caesar_cipher(text: str, shift: int, direction: str) -> str:
    """Encode or decode a message using the Caesar Cipher."""

    if direction == "decode":
        shift *= -1

    shift %= len(ALPHABET)

    result = ""

    for char in text:
        if char in ALPHABET:
            current_position = ALPHABET.index(char)
            new_position = (current_position + shift) % len(ALPHABET)
            result += ALPHABET[new_position]
        else:
            result += char

    return result