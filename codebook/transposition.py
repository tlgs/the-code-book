import math

from codebook.utils import validate


@validate
def rail_fence(plaintext, rails=2):
    """Rail Fence cipher; page 8"""
    filtered = [c for c in plaintext.upper() if c.isalpha()]

    return "".join(["".join(filtered[i::rails]) for i in range(rails)])


@validate
def scytale(plaintext, diameter):
    """Scytale cipher; page 8"""
    filtered = [c for c in plaintext.upper() if c.isalpha()]

    cols = math.ceil(len(filtered) / diameter)
    return "".join(["".join(filtered[i::cols]) for i in range(cols)])
