import string


def validate_plaintext(plaintext: str) -> str:
    if not plaintext.islower():
        raise ValueError("Plaintext should be lowercase.")

    return plaintext


def validate_key(key: str) -> str:
    if not key.isupper():
        raise ValueError("Key should be uppercase.")

    seen = set()
    filtered_key = []
    for c in filter(str.isalpha, key):
        if c not in seen:
            seen.add(c)
            filtered_key.append(c)

    return "".join(filtered_key)


def validate_cipher_alphabet(cipher_alphabet: str) -> str:
    if not set(cipher_alphabet) == set(string.ascii_uppercase):
        raise ValueError(
            "Cipher alphabet should be uppercase and contain all 26 letters."
        )

    return cipher_alphabet
