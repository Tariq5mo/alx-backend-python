#!/usr/bin/env python3
"""Type-annotation for function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.

Returns:
    float: returns sum of mxd_lst
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum_mxd_lst: float = 0.0
    for num in mxd_lst:
        sum_mxd_lst += num
    return float(sum_mxd_lst)
