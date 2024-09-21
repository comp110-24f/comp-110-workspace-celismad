"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730808435"


def input_word() -> str:
    """Collects a word input of 5 characters from the user"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter() -> str:
    """Collects a letter input from the user"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """Searches for the letter at each index of the word"""
    print("Searching for " + letter + " in " + word)  # Had to add an extra space
    # Originally had the below as "elif" statements after the first "if", but realized
    # that wasn't going to work because I needed it to go through every index.
    count = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    # had to add extra spaces at the beginning of the "found in" because it was
    # returning as "pfoundin" and the like
    # If statement has 3 conditions: for no instances, one instance, and more than one.
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:  # Added "None"
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
