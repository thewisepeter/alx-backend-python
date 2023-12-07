#!/usr/bin/env python3
''' type-annotated function make_multiplier'''

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
