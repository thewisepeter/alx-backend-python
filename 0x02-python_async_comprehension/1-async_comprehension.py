#!/usr/bin/env python3
'''
    Import async_generator from the previous task and then
    write a coroutine called async_comprehension that takes
    no arguments.

    The coroutine will collect 10 random numbers using an
    async comprehensing over async_generator, then return
    the 10 random numbers.
'''

from typing import List
async_generator = __import__('0-aync_generator').async_generator


async def async_generator() -> List[float]:
    ''' function that returns 10 random numbers '''
    random_numbers = [rand_num async for rand_num in async_generator()]

    return random_numbers