"""Cryptography substitution primitives"""
import itertools
import string

from codebook.utils import validate


def _shifted_alphabet(n):
    return (string.ascii_uppercase * 2)[n : n + 26]


@validate
def caesar(plaintext, shift):
    """Caesar cipher; page 10"""
    return generic(plaintext, _shifted_alphabet(shift % 26))


@validate
def generic(plaintext, cipher_alphabet):
    """Generic substitution cipher; page 12"""
    mapping = str.maketrans(dict(zip(string.ascii_lowercase, cipher_alphabet)))

    return plaintext.translate(mapping)


@validate
def keyphrase(plaintext, key):
    """Generic substitution using a keyphrase; page 13"""
    seen = set()
    squeezed = []
    for c in filter(str.isalpha, key):
        if c not in seen:
            seen.add(c)
            squeezed.append(c)

    start = ord(squeezed[-1]) - 65
    remaining = [c for c in _shifted_alphabet(start + 1) if c not in seen]

    return generic(plaintext, "".join(squeezed + remaining))


@validate
def vigenere(plaintext, key):
    """Vigenère cipher; page 48"""
    cycled_cipher_alphabet = itertools.cycle(
        _shifted_alphabet(ord(c) - 65) for c in key if c.isalpha()
    )

    ciphertext = [
        next(cycled_cipher_alphabet)[ord(c) - 97] if c.isalpha() else c
        for c in plaintext
    ]

    return "".join(ciphertext)
