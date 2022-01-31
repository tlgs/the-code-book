import string


def validate_plaintext(plaintext: str) -> str:
    if not plaintext.islower():
        raise ValueError("plaintext should be lowercase")

    return "".join(filter(str.isalnum, plaintext))


def validate_key(key: str) -> str:
    if not key.isupper():
        raise ValueError("key should be uppercase")

    squoze = []
    for c in filter(str.isalpha, key):
        if c not in squoze:
            squoze.append(c)

    return "".join(squoze)


def validate_cipher_alphabet(cipher_alphabet: str) -> str:
    if not set(cipher_alphabet) == set(string.ascii_uppercase):
        raise ValueError(
            "cipher alphabet should be uppercase and contain all 26 letters"
        )

    return cipher_alphabet
