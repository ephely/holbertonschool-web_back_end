#!/usr/bin/env python3
"""
Annotate the given function’s parameters
and return values with the appropriate types
"""


from typing import List, Tuple, Sized


def element_length(lst: List[Sized]) -> List[Tuple[Sized, int]]:
    """
    Function element_length returns a list.
    """
    return [(i, len(i)) for i in lst]
