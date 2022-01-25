import collections
import itertools
import math

from codebook.utils import validate_key, validate_plaintext


def rail_fence(plaintext: str, *, n: int = 2) -> str:
    """Rail Fence cipher; page 8"""
    plaintext = validate_plaintext(plaintext)

    filtered = [c for c in plaintext.upper() if c.isalpha()]

    return "".join(["".join(filtered[i::n]) for i in range(n)])


def scytale(plaintext: str, *, diameter: int) -> str:
    """Scytale cipher; page 8"""
    plaintext = validate_plaintext(plaintext)

    filtered = [c for c in plaintext.upper() if c.isalpha()]

    cols = math.ceil(len(filtered) / diameter)
    return "".join(["".join(filtered[i::cols]) for i in range(cols)])


def adfgvx(plaintext: str, *, key: str) -> str:
    """ADFGVX cipher; page 374"""
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
