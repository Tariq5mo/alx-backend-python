#!/usr/bin/env python3
"""
This module contains a type-annotated function sum_list which takes a list
input_list of floats as an argument and returns their sum as a float.

Functions:
    sum_list(input_list: List[float]) -> float:
        Returns the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of the float numbers in the list.
    """
    sum_float: float = 0.0
    for num in input_list:
        sum_float += num
    return sum_float
