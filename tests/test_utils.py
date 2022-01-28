from string import ascii_lowercase, ascii_uppercase

import pytest

from codebook.utils import validate_cipher_alphabet, validate_key, validate_plaintext


def test_validate_key():
    assert validate_key("JULIUS CAESAR") == "JULISCAER"


@pytest.mark.parametrize(
    "test_input",
    [
        pytest.param(ascii_lowercase[13:] + ascii_lowercase[:13], id="lowercase"),
        pytest.param(ascii_uppercase[-5:], id="incomplete"),
    ],
)
def test_validate_cipher_alphabet_raises(test_input):
    with pytest.raises(ValueError):
        validate_cipher_alphabet(test_input)


def test_validate_key_raises():
    with pytest.raises(ValueError):
        validate_key("lowercase key")


def test_validate_plaintext_raises():
    with pytest.raises(ValueError):
        validate_plaintext("UPPERCASE PLAINTEXT")
