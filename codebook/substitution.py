"""
This module defines a number of classical substitution ciphers.

It features different types of substitution ciphers:

  - Monoalphabetic: `caesar`, `generic`, `keyphrase`
  - Polyalphabetic: `vigenere`
  - Polygraphic: `playfair`
"""
import itertools
from string import ascii_lowercase, ascii_uppercase

from codebook.utils import (
    codegroup,
    validate_cipher_alphabet,
    validate_key,
    validate_plaintext,
)


def _shifted_alphabet(n: int) -> str:
    return ascii_uppercase[n:] + ascii_uppercase[:n]


def _keyed_alphabet(key: str, *, from_start: bool) -> str:
    seen = set(key)

    if from_start:
        remaining = [c for c in ascii_uppercase if c not in seen]
    else:
        start = ord(key[-1]) - 65
        remaining = [c for c in _shifted_alphabet(start + 1) if c not in seen]

    return key + "".join(remaining)


@codegroup
def caesar(plaintext: str, *, shift: int) -> str:
    """Caesar cipher (page 10)

    - `plaintext` is the message to be encrypted
    - `shift` is the number of places to rotate the plain alphabet (right shift)
    """
    alphabet = _shifted_alphabet(shift % 26)
    return generic(plaintext, cipher_alphabet=alphabet)


@codegroup
def generic(plaintext: str, *, cipher_alphabet: str) -> str:
    """Monoalphabetic substitution cipher (page 12)

    - `plaintext` is the message to be encrypted
    - `cipher_alphabet` is the cipher alphabet that represents the substitution
    """
    plaintext = validate_plaintext(plaintext)
    cipher_alphabet = validate_cipher_alphabet(cipher_alphabet)

    mapping = str.maketrans(ascii_lowercase, cipher_alphabet)

    return plaintext.translate(mapping)


@codegroup
def keyphrase(plaintext: str, *, key: str) -> str:
    """Monoalphabetic substitution cipher using a keyword/keyphrase (page 13)

    - `plaintext` is the message to be encrypted
    - `key` is the keyword or keyphrase used to generate the cipher alphabet

    As per the example in the book, the remainder of the alphabet starts
    where the keyphrase ends.
    For example, `JULIUS CAESAR` generates the `JULISCAERTVWXYZBDFGHKMNOPQ` alphabet
    and not `JULISCAERBDFGHKMNOPQTVWXYZ`, which is a common alternative.
    """
    key = validate_key(key)

    alphabet = _keyed_alphabet(key, from_start=False)
    return generic(plaintext, cipher_alphabet=alphabet)


@codegroup
def vigenere(plaintext: str, *, key: str) -> str:
    """Vigenère cipher (page 48)

    - `plaintext` is the message to be encrypted
    - `key` defines the series of interwoven Caesar ciphers to be used
    """
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    cycled_cipher_alphabet = itertools.cycle(
        _shifted_alphabet(ord(c) - 65) for c in key
    )

    seq = [next(cycled_cipher_alphabet)[ord(c) - 97] for c in plaintext]
    return "".join(seq)


@codegroup
def playfair(plaintext: str, *, key: str) -> str:
    """Playfair cipher (Appendix E, page 372)

    - `plaintext` is the message to be encrypted
    - `key` defines the 5x5 table used for encryption

    As per the example in the book, `J` and `I` share a space on the table
    and `x` is used as padding for *same-letter* digrams and for the *last space*,
    if required.
    """
    plaintext = validate_plaintext(plaintext)
    key = validate_key(key)

    # build matrix
    cipher_alphabet = list(_keyed_alphabet(key, from_start=True))
    cipher_alphabet.remove("J")

    from_char, to_char = {}, {}
    for i, c in enumerate(cipher_alphabet):
        y, x = divmod(i, 5)
        from_char[c] = (x, y)
        to_char[x, y] = c

    from_char["J"] = from_char["I"]

    # collect digraphs
    digraphs = []
    i = 0
    while i + 1 < len(plaintext):
        a, b = plaintext[i], plaintext[i + 1]
        if a != b:
            digraphs.append(a + b)
            i += 2
        else:
            digraphs.append(a + "x")
            i += 1

    if i < len(plaintext):
        digraphs.append(plaintext[i] + "x")

    # apply transfrom
    seq = []
    for digraph in digraphs:
        x, y = from_char[digraph[0].upper()]
        v, w = from_char[digraph[1].upper()]

        if y == w:
            a = to_char[(x + 1) % 5, y]
            b = to_char[(v + 1) % 5, y]
        elif x == v:
            a = to_char[x, (y + 1) % 5]
            b = to_char[x, (w + 1) % 5]
        else:
            a = to_char[v, y]
            b = to_char[x, w]

        seq.append(a + b)

    return "".join(seq)
