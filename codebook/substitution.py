"""Cryptography substitution primitives"""
import itertools
import string

from codebook.utils import validate_cipher_alphabet, validate_key, validate_plaintext


def _shifted_alphabet(n: int) -> str:
    return (string.ascii_uppercase * 2)[n : n + 26]


def _keyed_alphabet(key: str, *, from_start: bool = True) -> str:
    seen = []
    for c in filter(str.isalpha, key):
        if c not in seen:
            seen.append(c)

    if from_start:
        remaining = [c for c in string.ascii_uppercase if c not in seen]
    else:
        start = ord(seen[-1]) - 65
        remaining = [c for c in _shifted_alphabet(start + 1) if c not in seen]

    return "".join(seen + remaining)


def caesar(plaintext: str, shift: int) -> str:
    """Caesar cipher; page 10"""
    return generic(plaintext, _shifted_alphabet(shift % 26))


def generic(plaintext: str, cipher_alphabet: str) -> str:
    """Generic substitution cipher; page 12"""
    plaintext = validate_plaintext(plaintext)
    cipher_alphabet = validate_cipher_alphabet(cipher_alphabet)

    mapping = str.maketrans(dict(zip(string.ascii_lowercase, cipher_alphabet)))

    return plaintext.translate(mapping)


def keyphrase(plaintext: str, key: str) -> str:
    """Generic substitution using a keyphrase; page 13"""
    return generic(plaintext, _keyed_alphabet(key, from_start=False))


def vigenere(plaintext: str, key: str) -> str:
    """Vigenère cipher; page 48"""
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    cycled_cipher_alphabet = itertools.cycle(
        _shifted_alphabet(ord(c) - 65) for c in filter(str.isalpha, key)
    )

    ciphertext = [
        next(cycled_cipher_alphabet)[ord(c) - 97] if c.isalpha() else c
        for c in plaintext
    ]

    return "".join(ciphertext)


def playfair(plaintext: str, key: str) -> str:
    """Playfair cipher; page 372"""
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    # build matrix
    cipher_alphabet = list(_keyed_alphabet(key))
    cipher_alphabet.remove("J")
    char_to_coord, coord_to_char = {}, {}
    for i, c in enumerate(cipher_alphabet):
        x, y = (i % 5, i // 5)
        char_to_coord[c] = (x, y)
        coord_to_char[x, y] = c

    char_to_coord["J"] = char_to_coord["I"]

    # collect digraphs
    filtered = [c for c in plaintext if c.isalpha()]
    digraphs = []
    seen_two = False
    for a, b in itertools.pairwise(filtered):
        if seen_two:
            seen_two = False
            continue
        if a != b:
            digraphs.append(a + b)
            seen_two = True
        else:
            digraphs.append(a + "x")

    if digraphs[-1][-1] != filtered[-1]:
        digraphs.append(filtered[-1] + "x")

    # apply transfrom
    ciphertext = []
    for digraph in digraphs:
        x, y = char_to_coord[digraph[0].upper()]
        v, w = char_to_coord[digraph[1].upper()]

        if y == w:
            p = coord_to_char[(x + 1) % 5, y]
            q = coord_to_char[(v + 1) % 5, y]
        elif x == v:
            p = coord_to_char[x, (y + 1) % 5]
            q = coord_to_char[x, (w + 1) % 5]
        else:
            p = coord_to_char[v, y]
            q = coord_to_char[x, w]

        ciphertext.append(p + q)

    return " ".join(ciphertext)
