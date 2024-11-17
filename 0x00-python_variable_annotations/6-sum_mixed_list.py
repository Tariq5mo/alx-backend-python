#!/usr/bin/env python3
"""
This module contains a type-annotated function sum_mixed_list
which takes a list
mxd_lst of integers and floats and returns their sum as a float.

Functions:
    sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
        Returns the sum of a list of integers and floats
        as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and
        float numbers.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return sum(mxd_lst)
