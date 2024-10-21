"""Summing the elements of a list using different loops"""

__author__ = "730808435"

import pytest

from exercises.ex05.utils import (
    only_evens,
    sub,
    add_at_index,
)  # imports functions from utils


def test_evens_input() -> None:
    """Tests that only_evens does not modify the input"""
    original_list: list[int] = [1, 2, 3]
    only_evens(original_list)
    assert original_list == [1, 2, 3]


def test_evens_output() -> None:
    """Tests that only_evens returns the correct output"""
    assert (only_evens([1, 2, 3])) == [2]


def test_evens_edge_case() -> None:
    """Tests that only_evens returns the correct list in an edge case"""
    assert only_evens([]) == ([])


def test_sub_input() -> None:
    """Tests that sub does not modify the input"""
    old_list: list[int] = [10, 20, 30, 50]
    sub(old_list, 1, 3)
    assert old_list == [10, 20, 30, 50]


def test_sub_output() -> None:
    """Tests that sub returns the correct output"""
    assert sub([1, 2, 3], 1, 2) == [2]


def test_sub_edge_case() -> None:
    """Tests that sub functions with an edge case"""
    assert sub([1, 2, 3, 4], -6, -8) == []


def test_add_at_index_input() -> None:
    """Tests that add_at_input modifies the input correctly"""
    old_list: list[int] = [1, 2, 3]
    add_at_index(old_list, 1, 2)
    assert old_list == [1, 2, 1, 3]


def test_add_at_index_output() -> None:
    """Tests that add_at_input returns the correct output"""
    assert add_at_index([1, 2], 0, 1) == None


def test_add_at_index_edge_case() -> None:
    """Tests that the function raises an IndexError if the index is invalid"""
    with pytest.raises(IndexError):
        add_at_index([0, 2], 1, 3)
