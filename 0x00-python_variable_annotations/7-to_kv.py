#!/usr/bin/env python3
"""
This module contains a type-annotated function to_kv that takes a string k
and an int or float v as arguments and returns a tuple. The first element
of the tuple is the string k. The second element is
the square of the int/float v.

Functions:
    to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
        Returns a tuple with the string k and
        the square of the int/float v.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k and the square of the int/float v.

    Args:
        k (str): The string value.
        v (Union[int, float]): The int or float value to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string k
                           and the second element is
                           the square of v as a float.
    """
    return (k, float(v ** 2))
