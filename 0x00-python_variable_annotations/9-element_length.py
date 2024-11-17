#!/usr/bin/env python3
"""Annotation the below function's parameters and return values
with the appropriate types:

def element_length(lst):
    return [(i, len(i)) for i in lst]

Returns:
    List[Tuple[Sequence, int]]
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
