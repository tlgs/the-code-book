"""Cryptography substitution primitives"""
import itertools
import string

from codebook.utils import validate_cipher_alphabet, validate_key, validate_plaintext


def _shifted_alphabet(n: int) -> str:
    return (string.ascii_uppercase * 2)[n : n + 26]


def caesar(plaintext: str, shift: int) -> str:
    """Caesar cipher; page 10"""
    plaintext = validate_plaintext(plaintext)
    return generic(plaintext, _shifted_alphabet(shift % 26))


def generic(plaintext: str, cipher_alphabet: str) -> str:
    """Generic substitution cipher; page 12"""
    plaintext = validate_plaintext(plaintext)
    cipher_alphabet = validate_cipher_alphabet(cipher_alphabet)

    mapping = str.maketrans(dict(zip(string.ascii_lowercase, cipher_alphabet)))

    return plaintext.translate(mapping)


def keyphrase(plaintext: str, key: str) -> str:
    """Generic substitution using a keyphrase; page 13"""
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    seen = set()
    squeezed = []
    for c in filter(str.isalpha, key):
        if c not in seen:
            seen.add(c)
            squeezed.append(c)

    start = ord(squeezed[-1]) - 65
    remaining = [c for c in _shifted_alphabet(start + 1) if c not in seen]

    return generic(plaintext, "".join(squeezed + remaining))


def vigenere(plaintext: str, key: str) -> str:
    """Vigenère cipher; page 48"""
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    cycled_cipher_alphabet = itertools.cycle(
        _shifted_alphabet(ord(c) - 65) for c in key if c.isalpha()
    )

    ciphertext = [
        next(cycled_cipher_alphabet)[ord(c) - 97] if c.isalpha() else c
        for c in plaintext
    ]

    return "".join(ciphertext)
