#!/usr/bin/env python3
''' type-annotated function '''

from typing import Union, Any, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Duck type '''
    if lst:
        return lst[0]
    else:
        return None
