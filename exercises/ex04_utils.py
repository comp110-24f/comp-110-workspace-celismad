"""Reverse engineers a series of functions."""

__author__ = "730808435"


def all(vals: list[int], compare: int) -> bool:
    """Checks if every value in a list equals a given value"""
    if vals == []:
        return False
    for (
        val
    ) in (
        vals
    ):  # For loop runs through the list and returns false if it finds a value that
        # != 'compare'
        if val != compare:
            return False
    return True


def max(vals: list[int]) -> int:
    """Finds the maximum value in a list"""
    if len(vals) == 0:
        raise ValueError("max() arg  is an empty list")
    greatest: int = vals[0]  # Sets "greatest" as the first item in the list
    for (
        val
    ) in vals:  # For loop that replaces "greatest" if it comes across a greater number
        if val > greatest:
            greatest = val
    return greatest


def is_equal(vals: list[int], vals_equal: list[int]) -> bool:
    """Returns True if every value in both lists is equal"""
    if len(vals) != len(vals_equal):  # Makes sure the list lengths are equal
        return False
    i = 0
    while i < len(vals):  # Runs through each item in the lists to check their equality
        if vals[i] != vals_equal[i]:
            return False
        i += 1
    return True


def extend(vals: list[int], vals_append: list[int]) -> None:
    """Appends the items in 'vals2' to 'vals'"""
    i = 0
    while i < len(vals_append):  # Goes through each item in vals2 to append to vals
        vals.append(vals_append[i])
        i += 1
