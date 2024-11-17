#!/usr/bin/env python3
"""Type-annotation for function make_multiplier
that takes a float multiplier as argument and returns a function

Returns:
    Function: multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def func(num: float) -> float:
        return num * multiplier
    return func
