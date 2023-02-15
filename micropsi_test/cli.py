import argparse
from typing import Sequence

from micropsi_test import find_min

_DESC = """
Find the minimum element in sequence using as few comparisons as possible.
The array shall be given such that the first elements are strictly monotonically
decreasing, the remaining elements are strictly monotonically increasing.
"""


class Arguments:
    numbers: list[float]


def parse_args(args: Sequence[str] | None = None) -> Arguments:
    """
    >>> parse_args([])  # will print usage to stderr
    Traceback (most recent call last):
        ...
    SystemExit: 2
    >>> parse_args(['1']).numbers
    [1.0]
    >>> parse_args('1 2 3'.split()).numbers
    [1.0, 2.0, 3.0]
    """
    parser = argparse.ArgumentParser(prog="micropsi_test", description=_DESC)
    parser.add_argument(
        "numbers",
        metavar="N",
        nargs="+",
        type=float,
        help="Numbers in sequence (converted to float)",
    )
    return parser.parse_args(args, namespace=Arguments())


def main() -> None:  # pragma: no cover
    args = parse_args()
    print(find_min(args.numbers))
