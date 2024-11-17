#!/usr/bin/env python3
"""
This module contains a type-annotated function element_length
that takes an iterable of sequences and returns
a list of tuples.
Each tuple contains a sequence from the input and its length.

Functions:
    element_length(lst: Iterable[Sequence])->List[Tuple[Sequence, int]]:
        Returns a list of tuples with each sequence and its length.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
    contains a sequence from the input and its length.
    """
    return [(i, len(i)) for i in lst]
