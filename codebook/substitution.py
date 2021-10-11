import string


def _shifted_alphabet(n):
    return (string.ascii_uppercase * 2)[n : n + 26]


def caesar(message, shift):
    """Caesar cipher; page 10"""
    return general(message, _shifted_alphabet(shift % 26))


def general(message, cipher_alphabet):
    """General substitution cipher; page 12"""
    mapping = str.maketrans(dict(zip(string.ascii_lowercase, cipher_alphabet)))

    return message.translate(mapping)


def keyphrase(message, key):
    """General substitution using a keyphrase; page 13"""
    seen = set()
    squeezed = []
    for c in filter(str.isalpha, key.upper()):
        if c not in seen:
            seen.add(c)
            squeezed.append(c)

    start = ord(squeezed[-1]) - 65
    remaining = [c for c in _shifted_alphabet(start + 1) if c not in seen]

    return general(message, "".join(squeezed + remaining))
