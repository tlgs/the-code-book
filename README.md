# The Code Book

This is a _code along_ to Simon Singh's
[The Code Book](https://simonsingh.net/books/the-code-book/)
(ISBN 978-1-85702-889-8).

Only **encryption operations** are implemented.

## Motivation

- implement cryptographic primitives using standard Python
- mess around with [pytest](https://docs.pytest.org/)/[coverage](https://coverage.readthedocs.io)
  to power a _test-first_ development cycle
- design a Python package with a sensible API (complete with lightweight documentation)

## Development notes

- install and setup project with `pip install -e .[dev]` and `pre-commit install`
- run tests with `coverage run` and inspect results with `coverage report`
- generate documentation with `pdoc -o docs --no-search codebook`

## Disclaimer

This project is meant purely as an exercise to absorb the contents of the book.
**Should not be seen as a reference towards applying any cryptographic technique.**
