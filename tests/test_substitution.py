import pytest

from codebook.substitution import caesar, generic, keyphrase, playfair, vigenere


def test_caesar():
    assert caesar("veni, vidi, vici", shift=3) == "YHQLYLGLYLFL"


def test_generic():
    assert (
        generic("et tu, brute?", cipher_alphabet="JLPAWIQBCTRZYDSKEGFXHUONVM")
        == "WXXHLGHXW"
    )


def test_keyphrase():
    assert keyphrase("et tu, brute?", key="JULIUS CAESAR") == "SHHKUFKHS"


def test_vigenere():
    assert (
        vigenere("divert troops to east ridge", key="WHITE")
        == "ZPDXVPAZHSLZBHIWZBKMZNM"
    )


@pytest.mark.parametrize(
    "plaintext, key, expected",
    [
        pytest.param(
            "meet me at hammersmith bridge tonight",
            "CHARLES",
            "GD DO GD RQ AR KY GD HD NK PR DA MS OG UP GK IC QY",
            id="pad last space",
        ),
        pytest.param(
            "hide the gold in the tree stump",
            "PLAYFAIR EXAMPLE",
            "BM OD ZB XD NA BE KU DM UI XM MO UV IF",
            id="no padding",
        ),
    ],
)
def test_playfair(plaintext, key, expected):
    assert playfair(plaintext, key=key) == expected
