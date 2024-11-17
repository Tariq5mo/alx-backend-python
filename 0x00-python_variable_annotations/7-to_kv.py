#!/usr/bin/env python3
"""Type-annotated for function to_kv
that takes a string k and an int OR float v as arguments

Returns:
    tuple: The first element of the tuple is the string k.
    The second element is the square of the int/float v
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)
