"""
Given an array of elements that provide a less than operator,
find the minimum using as few comparisons as possible.
The array shall be given such that the first elements are strictly
monotonically decreasing, the remaining elements are strictly monotonically increasing.
The less than operator be defined as the operator that works
on such vectors where a < b if min(a,b) == a.
"""

from collections.abc import Sequence
from typing import Any, Protocol, TypeVar


# basically a copy from ``typeshed``
class SupportsLessThan(Protocol):
    def __lt__(self, other: Any, /) -> bool:
        # NOTE: having ``other`` as positional only argument
        #   is important because builtin types name this argument
        #   differently. If ``other`` is not set as positional
        #   only then type checker would (rightfully) complain
        #   about incompatible signatures.
        ...  # pragma: no cover


# basically a copy from ``typeshed``
SupportsLessThanT = TypeVar("SupportsLessThanT", bound=SupportsLessThan)


def _given_conditions_apply(arg: Sequence[SupportsLessThanT]) -> bool:
    # convenience function for debug
    from itertools import pairwise

    # if sequence is correct then minimal element should be unique
    # and everything to its left should decrease while everything
    # to the right should increase
    min_idx = arg.index(min(arg))
    first_strictly_decreasing = all(b < a for a, b in pairwise(arg[: min_idx + 1]))
    remaining_strictly_increasing = all(a < b for a, b in pairwise(arg[min_idx:]))
    return first_strictly_decreasing and remaining_strictly_increasing


def find_min(arg: Sequence[SupportsLessThanT], /) -> SupportsLessThanT:
    """
    Given an array, where first elements are strictly monotonically
    decreasing and remaining are strictly monotonically increasing,
    find the minimum using as few comparisons as possible.

    >>> find_min([1])
    1
    >>> find_min([0, 1])
    0
    >>> find_min([1, 0])
    0
    >>> find_min([3, 2, 1, 4, 5])
    1
    >>> find_min([3, 2, 1, 0, 1])
    0
    >>> find_min([4, 3, 2, 1, 0])
    0
    >>> find_min([1, 2, 3, 4, 5])
    1
    >>> find_min([1, 0, 1, 2, 3])
    0
    >>> find_min([])
    Traceback (most recent call last):
        ...
    ValueError: find_min() arg is an empty sequence
    >>> find_min([1, 2, 3, 2, 1])
    Traceback (most recent call last):
        ...
    AssertionError: Provided sequence does not satisfy conditions
    """
    if not arg:
        raise ValueError("find_min() arg is an empty sequence")

    # sanity check for debug. can be disabled with ``-O`` flag to python
    assert _given_conditions_apply(arg), 'Provided sequence does not satisfy conditions'

    low_idx, high_idx = 0, len(arg) - 1

    while low_idx < high_idx:
        mid_idx = (high_idx + low_idx) // 2
        if arg[mid_idx] < arg[mid_idx + 1]:
            high_idx = mid_idx
        else:
            low_idx = mid_idx + 1
    return arg[low_idx]
