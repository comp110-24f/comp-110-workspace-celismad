"""Writes functions that call other functions to make one coherent program."""

__author__ = "730808435"


def main_planner(guests: int) -> None:
    """entrypoint of the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Calculate tea_bags and treats first before going to cost
    # Had to add "str" before all of my integers so they could be added into the strings
    teabags = tea_bags(people=guests)
    treatcount = treats(people=guests)
    print("Tea Bags: " + str(teabags))
    print("Treats: " + str(treatcount))
    price = cost(tea_count=teabags, treat_count=treatcount)
    print("Cost: " + str(price))
    return None


def tea_bags(people: int) -> int:
    """Returns how many tea bags will be needed based on how many people are at the party."""
    return people * 2


def treats(people: int) -> int:
    """returns how many treats the party will require per person"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """computes the cost of treats and teabags combined"""
    # Need the count of treats and tea_bags for this function... so call the tea_bags and treats functions here?
    # That doesn't seem to make an awful lot of sense, considering that I'm supposed to go in with the values for tea_count and treat_count
    # Sent these numbers to main_planner first before sending them here?
    price = tea_count * 0.5 + treat_count * 0.75
    return price


if __name__ == "__main__":
    # Apparently this bit is "unreachable"?
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
