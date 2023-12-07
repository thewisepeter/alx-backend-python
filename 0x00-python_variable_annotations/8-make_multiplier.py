#!/usr/bin/env python3
''' type-annotated function make_multiplier'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        function make_multiplier that takes a float multiplier
        as argument and returns a function that multiplies a
        float by multiplier
    '''

    def float_multiplier(x: float) -> float:
        return multiplier * x

    return float_multiplier
