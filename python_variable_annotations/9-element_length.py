#!/usr/bin/env python3
from typing import List, Tuple, Sized

def element_length(lst: List[Sized]) -> List[Tuple[Sized, int]]:
    return [(i, len(i)) for i in lst]