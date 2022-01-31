import pytest

from codebook.substitution import caesar, generic, keyphrase, playfair, vigenere


def test_caesar():
    assert caesar("veni, vidi, vici", shift=3) == "YHQL, YLGL, YLFL"


def test_generic():
    assert (
        generic("et tu, brute?", cipher_alphabet="JLPAWIQBCTRZYDSKEGFXHUONVM")
        == "WX XH, LGHXW?"
    )


def test_keyphrase():
    assert keyphrase("et tu, brute?", key="JULIUS CAESAR") == "SH HK, UFKHS?"


def test_vigenere():
    assert (
        vigenere("divert troops to east ridge", key="WHITE")
        == "ZPDXVP AZHSLZ BH IWZB KMZNM"
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
            id="full length",
        ),
    ],
)
def test_playfair(plaintext, key, expected):
    assert playfair(plaintext, key=key) == expected
