# Micropsi Industries test

This package is a solution to [Micropsi Industries](https://www.micropsi-industries.com/)
test.

## Building

[`hatch`](https://hatch.pypa.io/latest/) is used to build the package.

```shell
hatch build
```

This will build source distribution and wheel and place them to `dist` directory.

## Installation

Using pip install and wheel from build stage.

```shell
# assuming wheel already in cwd
python3 -m pip install micropsi_test-0.0.1-py3-none-any.whl
```

## Usage

### From CLI

```shell
python3 -m micropsi_test --help  # prints usage
python3 -m micropsi_test 3 2 1 4 5  # 1.0
```

### As a package

```python
from micropsi_test import find_min

find_min([3, 2, 1, 4, 5])  # 1
```

## Notes on testing

Testing is done using `doctest` and runs using `pytest`. To run them either use
`hatch` or `pytest` directly (flag `--doctest-modules` is specified in `pyproject.toml`).

```shell
hatch run cov  # if you'd like to see coverage
hatch run no-cov  # without coverage
pytest
```

## Test description

Implement a Python module, which can be installed using pip, including tests,
with the following functionality: Given an array of elements that provide a less than
operator, find the minimum using as few comparisons as possible. The array shall be
given such that the first elements are strictly monotonically decreasing, the remaining
elements are strictly monotonically increasing. The less than operator be defined as the
operator that works on such vectors where a < b if min(a,b) == a.
