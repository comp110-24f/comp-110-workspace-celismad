"""Runs a game of Wordle with 6 turns."""

__author__ = "730808435"


def input_guess(secret_word_len: int) -> str:
    """Prompts the used for a guess until they input one of the correct number of
    characters."""
    guess: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # Altered to include an f-string
    i: int = 0
    if len(guess) == secret_word_len:
        return guess
    else:
        # If the word is the wrong length, loops asking for a new word till it is 5
        # chars.
        while i == 0:
            guess: str = input(f"That wasn't {secret_word_len} chars! Try again: ")
            if len(guess) == secret_word_len:
                i += 1
                return guess


def contains_char(searched_through: str, searched_for: str) -> bool:
    """Checks each index of a string to see if it matches the character being searched
    for."""
    assert len(searched_for) == 1
    i: int = 0  # signifies the index being checked
    while i < len(searched_through):
        # Looks for the character in the word
        if searched_through[i] == searched_for:
            return True
        i += 1
    return False  # returns false if the searched_fors character isn't found at all


def emojified(user_guess: str, secret_word: str) -> str:
    """Creates an emoji string symbolizing if the guesses of each character is correct
    at the given index, or if the character is in the word at all."""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    returnstring: str = ""
    while i < len(secret_word):
        if secret_word[i] == user_guess[i]:
            # Adds a green box if the characters are the same at the given index
            returnstring += GREEN_BOX
        elif contains_char(secret_word, user_guess[i]):
            # Adds a yellow box if the character is in the word, but at a different
            # index.
            returnstring += YELLOW_BOX
        else:
            # Adds a white box if the character does not appear at all
            returnstring += WHITE_BOX
        i += 1
    return returnstring


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    while i < 7:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(len(secret))
        returnstring: str = emojified(
            guess, secret
        )  # Takes the user input and secret word as parameters before running emojified
        print(returnstring)
        if guess == secret:
            print(f"You won in {i}/6 turns!")
            i = 8  # Ends the loop while ensuring that it won't trigger the losing
            # message
        else:
            i += 1
    if (
        i == 7
    ):  # If nothing was found, the loop will have been exited with i = 7, so that
        # value can trigger the losing message
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
