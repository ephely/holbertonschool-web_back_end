#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function sum_mixed_list returns the sum of
    int and floats of a list as a float.
    """
    return sum(mxd_lst)
