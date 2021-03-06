# Stubs for django.utils.tree (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class Node:
    default = ... # type: Any
    children = ... # type: Any
    connector = ... # type: Any
    negated = ... # type: Any
    def __init__(self, children=None, connector=None, negated=False): ...
    def __deepcopy__(self, memodict): ...
    def __len__(self): ...
    def __bool__(self): ...
    def __nonzero__(self): ...
    def __contains__(self, other): ...
    def add(self, data, conn_type, squash=True): ...
    def negate(self): ...
