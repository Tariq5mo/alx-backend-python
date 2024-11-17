#!/usr/bin/env python3
"""
This module contains a type-annotated function make_multiplier that
takes a float
multiplier as an argument and returns a function that multiplies
a float by the multiplier.

Functions:
    make_multiplier(multiplier: float) -> Callable[[float], float]:
        Returns a function that multiplies a float
        by the given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that
        multiplies a float by the multiplier.
    """
    def func(num: float) -> float:
        return num * multiplier
    return func
