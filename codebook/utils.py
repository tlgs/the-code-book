import string


def validate_plaintext(plaintext):
    if not plaintext.islower():
        raise ValueError("Plaintext should be lowercase.")

    return plaintext


def validate_key(key):
    if not key.isupper():
        raise ValueError("Key should be uppercase.")

    return key


def validate_cipher_alphabet(cipher_alphabet):
    if not set(cipher_alphabet) == set(string.ascii_uppercase):
        raise ValueError(
            "Cipher alphabet should be uppercase and contain all 26 letters."
        )

    return cipher_alphabet
