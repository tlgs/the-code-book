"""
This module defines a number of classical transposition ciphers.

It features simple ciphers like the `rail_fence` and the `scytale`,
as well as the fractionating transposition cipher `adfgvx`.
"""
import collections
import itertools
import math

from codebook.utils import validate_key, validate_plaintext


def rail_fence(plaintext: str, *, n: int = 2) -> str:
    """Rail Fence cipher (page 8)

    - `plaintext` is the message to be encrypted
    - `n` is the number of rails to use
    """
    plaintext = validate_plaintext(plaintext)

    filtered = [c for c in plaintext.upper() if c.isalpha()]

    seqs = collections.defaultdict(list)
    zigzag = itertools.cycle(itertools.chain(range(n), range(n - 2, 0, -1)))
    for i, c in zip(zigzag, filtered):
        seqs[i].append(c)

    return "".join(["".join(seqs[i]) for i in range(n)])


def scytale(plaintext: str, *, diameter: int) -> str:
    """Scytale cipher (page 8)

    - `plaintext` is the message to be encrypted
    - `diameter` is the number of letters that *can fit around the rod's circumference*
    """
    plaintext = validate_plaintext(plaintext)

    filtered = [c for c in plaintext.upper() if c.isalpha()]

    cols = math.ceil(len(filtered) / diameter)
    return "".join(["".join(filtered[i::cols]) for i in range(cols)])


def adfgvx(plaintext: str, *, key: str) -> str:
    """ADFGVX cipher (Appendix F, page 374)

    - `plaintext` is the message to be encrypted
    - `key` is the keyword or keyphrase used for the transposition stage of the cipher

    For practical purposes, the ADFGVX cipher uses two different keys: a 36 symbol
    alphabet to encode the 6x6 grid, and a keyword/keyphrase for the transposition
    stage.
    For simplicity, the grid's values are hardcoded with book's example:

    |       | **A** | **D** | **F** | **G** | **V** | **X** |
    | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
    | **A** |   8   |   p   |   3   |   d   |   1   |   n   |
    | **D** |   l   |   t   |   4   |   o   |   a   |   h   |
    | **F** |   7   |   k   |   b   |   c   |   5   |   z   |
    | **G** |   j   |   u   |   6   |   w   |   g   |   m   |
    | **V** |   x   |   s   |   v   |   i   |   r   |   2   |
    | **X** |   9   |   e   |   y   |   0   |   f   |   q   |
    """
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    lookup = {}
    for i, c in enumerate("8p3d1nlt4oah7kbc5zju6wgmxsvir29ey0fq"):
        x, y = i % 6, i // 6
        lookup[c] = "ADFGVX"[y] + "ADFGVX"[x]

    stage_one = "".join(lookup[c] for c in filter(str.isalnum, plaintext))

    columns = collections.defaultdict(list)
    for k, c in zip(itertools.cycle(key), stage_one):
        columns[k].append(c)

    result = itertools.chain(*[columns[k] for k in sorted(key)])
    return " ".join(result)
