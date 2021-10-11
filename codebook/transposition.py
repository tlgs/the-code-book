import math


def rail_fence(message, rails=2):
    """Rail Fence cipher; page 8"""
    filtered = [c for c in message.upper() if c.isalpha()]

    return "".join(["".join(filtered[i::rails]) for i in range(rails)])


def scytale(message, diameter):
    """Scytale cipher; page 8"""
    filtered = [c for c in message.upper() if c.isalpha()]

    cols = math.ceil(len(filtered) / diameter)
    return "".join(["".join(filtered[i::cols]) for i in range(cols)])
