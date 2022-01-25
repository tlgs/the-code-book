"""Cryptography substitution primitives"""
import itertools
import string

from codebook.utils import validate_cipher_alphabet, validate_key, validate_plaintext


def _shifted_alphabet(n: int) -> str:
    return (string.ascii_uppercase * 2)[n : n + 26]


def _keyed_alphabet(key: str, *, from_start: bool) -> str:
    seen = set(key)

    if from_start:
        remaining = [c for c in string.ascii_uppercase if c not in seen]
    else:
        start = ord(key[-1]) - 65
        remaining = [c for c in _shifted_alphabet(start + 1) if c not in seen]

    return key + "".join(remaining)


def caesar(plaintext: str, *, shift: int) -> str:
    """Caesar cipher; page 10"""
    alphabet = _shifted_alphabet(shift % 26)
    return generic(plaintext, cipher_alphabet=alphabet)


def generic(plaintext: str, *, cipher_alphabet: str) -> str:
    """Generic substitution cipher; page 12"""
    plaintext = validate_plaintext(plaintext)
    cipher_alphabet = validate_cipher_alphabet(cipher_alphabet)

    mapping = str.maketrans(dict(zip(string.ascii_lowercase, cipher_alphabet)))

    return plaintext.translate(mapping)


def keyphrase(plaintext: str, *, key: str) -> str:
    """Generic substitution using a keyphrase; page 13"""
    key = validate_key(key)

    alphabet = _keyed_alphabet(key, from_start=False)
    return generic(plaintext, cipher_alphabet=alphabet)


def vigenere(plaintext: str, *, key: str) -> str:
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


def playfair(plaintext: str, *, key: str) -> str:
    """Playfair cipher; page 372"""
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    # build matrix
    cipher_alphabet = list(_keyed_alphabet(key, from_start=True))
    cipher_alphabet.remove("J")

    char_to_coord, coord_to_char = {}, {}
    for i, c in enumerate(cipher_alphabet):
        x, y = (i % 5, i // 5)
        char_to_coord[c] = (x, y)
        coord_to_char[x, y] = c

    char_to_coord["J"] = char_to_coord["I"]

    # collect digraphs
    digraphs = []
    filtered = [c for c in plaintext if c.isalpha()]
    i = 0
    while i + 1 < len(filtered):
        a, b = filtered[i], filtered[i + 1]
        if a != b:
            digraphs.append(a + b)
            i += 2
        else:
            digraphs.append(a + "x")
            i += 1

    if i < len(filtered):
        digraphs.append(filtered[i] + "x")

    # apply transfrom
    ciphertext = []
    for digraph in digraphs:
        x, y = char_to_coord[digraph[0].upper()]
        v, w = char_to_coord[digraph[1].upper()]

        if y == w:
            a = coord_to_char[(x + 1) % 5, y]
            b = coord_to_char[(v + 1) % 5, y]
        elif x == v:
            a = coord_to_char[x, (y + 1) % 5]
            b = coord_to_char[x, (w + 1) % 5]
        else:
            a = coord_to_char[v, y]
            b = coord_to_char[x, w]

        ciphertext.append(a + b)

    return " ".join(ciphertext)
