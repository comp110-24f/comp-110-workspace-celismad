"""Exercise 06: 5 functions involving dictionaries"""

__author__ = "730808435"


def invert(dict_initial: dict[str, str]) -> dict[str, str]:
    """Makes a new dictionary with the keys and values of the initial dictionary
    swapped"""
    new_dict: dict[str, str] = {}  # creating the new dictionary.
    for value in dict_initial:
        i = 0
        for value_2 in dict_initial:  # Checks if the new key appears more than twice
            if dict_initial[value] == dict_initial[value_2]:
                i += 1
            if i == 2:
                raise KeyError("KeyError!")
        new_dict[dict_initial[value]] = value  # Adds new value to new_dict
    return new_dict


def favorite_color(name_color: dict[str, str]) -> str:
    """Finds the most common favorite color from a list"""
    values_dict: dict[str, int] = {}
    for (
        value
    ) in name_color:  # Adding to the dictionary of frequency colors have been said
        if name_color[value] in values_dict:
            values_dict[name_color[value]] += 1
        else:
            values_dict[name_color[value]] = 1
    greatest_value: int = 0
    return_string: str = ""  # Defining string to be returned
    for value in values_dict:
        if (
            values_dict[value] > greatest_value
        ):  # Tests if this value is greater than the current greatest
            greatest_value = values_dict[value]
            return_string = value
    return return_string


def count(values_old: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list"""
    new_dict: dict[str, int] = {}  # Creating the new dictionary
    for item in values_old:
        if item in new_dict:  # Adds one if the item is already in the dictionary
            new_dict[item] += 1
        else:  # Adds item to the dictionary if it isn't
            new_dict[item] = 1
    return new_dict


def alphabetizer(old_list: list[str]) -> dict[str, list[str]]:
    """Makes a dictionary with lists of strings that start with the same letter"""
    counted_dict: dict[str, list[str]] = {}
    for item in old_list:
        if item[0].lower() in counted_dict:  # Checks if string is in the dictionary
            counted_dict[item[0].lower()].append(
                item
            )  # Adds item to its letter in the dictionary
        else:
            counted_dict[item[0].lower()] = [
                item
            ]  # Adds item to its letter in the dictionar
    return counted_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Adds new values to the original dictionary (mutates it)"""
    if day in attendance:
        attendance[day].append(student)  # Adds student to the day if it already exists
    else:
        attendance[day] = [student]  # Adds day and student if it doesn't
