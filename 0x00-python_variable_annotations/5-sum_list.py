#!/usr/bin/env python3
"""type-annotation for function sum_list
which takes a list input_list of floats as argument and
returns their sum as a float.

Returns:
    float: sum of input_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum_float: float = 0.0
    for num in input_list:
        sum_float += num
    return float(sum_float)
