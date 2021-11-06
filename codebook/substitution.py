import string


def _shifted_alphabet(n):
    return (string.ascii_uppercase * 2)[n : n + 26]


def caesar(message, shift):
    """Caesar cipher; page 10"""
    return generic(message, _shifted_alphabet(shift % 26))


def generic(message, cipher_alphabet):
    """Generic substitution cipher; page 12"""
    mapping = str.maketrans(dict(zip(string.ascii_lowercase, cipher_alphabet)))

    return message.translate(mapping)


def keyphrase(message, key):
    """Generic substitution using a keyphrase; page 13"""
    seen = set()
    squeezed = []
    for c in filter(str.isalpha, key.upper()):
        if c not in seen:
            seen.add(c)
            squeezed.append(c)

    start = ord(squeezed[-1]) - 65
    remaining = [c for c in _shifted_alphabet(start + 1) if c not in seen]

    return generic(message, "".join(squeezed + remaining))
