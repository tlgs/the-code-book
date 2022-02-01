import functools
import string
import textwrap
from typing import Callable


def validate_plaintext(plaintext: str) -> str:
    if not plaintext.islower():
        raise ValueError("plaintext should be lowercase")

    return "".join(filter(str.isalnum, plaintext))


def validate_key(key: str) -> str:
    if not key.isupper():
        raise ValueError("key should be uppercase")

    seq = []
    for c in filter(str.isalpha, key):
        if c not in seq:
            seq.append(c)

    return "".join(seq)


def validate_cipher_alphabet(cipher_alphabet: str) -> str:
    if not set(cipher_alphabet) == set(string.ascii_uppercase):
        raise ValueError(
            "cipher alphabet should be uppercase and contain all 26 letters"
        )

    return cipher_alphabet


def codegroup(func: Callable[..., str]) -> Callable[..., str]:
    @functools.wraps(func)
    def wrapper(*args: str, **kwargs: str | int) -> str:
        ret = func(*args, **kwargs)
        return " ".join(textwrap.wrap(ret, 5))

    return wrapper
