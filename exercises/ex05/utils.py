"""Various functions creating new lists or altering old ones"""

__author__ = "730808435"


def only_evens(old_list: list[int]) -> list[int]:
    """Returns a new list with only the even values of an old list"""
    new_list: list[int] = []
    for (
        val
    ) in (
        old_list
    ):  # for loop runs through each variable in oldlist to check if it's even
        if (val % 2) == 0:
            new_list.append(val)
    return new_list


def sub(old_list: list[int], start_num: int, end_num: int) -> list[int]:
    """Creates a new list by identifying a start and an end index in the original
    list"""
    i: int = 0
    new_list: list[int] = []  # creates the empty new list
    while i < len(old_list):
        if (
            i >= start_num and i < end_num
        ):  # Checks if the index is after the "start" number and before
            # the "end" number
            new_list.append(old_list[i])
        i += 1
    return new_list


def add_at_index(old_list: list[int], var: int, var_2: int) -> None:
    """Adds an item to a list at a given index"""
    old_list.append(
        0
    )  # Adding a meaningless value to the end of the list so it can be replaced
    if var_2 < 0 or var_2 >= len(old_list):
        raise IndexError("Index is out of bounds for the input list")
    i: int = len(old_list) - 1
    while i > var_2:
        old_list[i] = old_list[
            i - 1
        ]  # Shifts each value up an index if it's above var_2
        i -= 1
    old_list[var_2] = var
    print(old_list)
