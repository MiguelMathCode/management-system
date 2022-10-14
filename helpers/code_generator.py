from random import choice
from string import ascii_uppercase, digits


def code_generator(length: int) -> str:
    " Function that generates randomg codes. Whereas for booking code or employee id"
    characters = ascii_uppercase + digits
    return "".join(choice(characters) for i in range(length))
