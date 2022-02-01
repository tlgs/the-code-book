import pytest

from codebook.substitution import caesar, generic, keyphrase, playfair, vigenere


def test_caesar():
    assert caesar("veni, vidi, vici", shift=3) == "YHQLY LGLYL FL"


def test_generic():
    assert (
        generic("et tu, brute?", cipher_alphabet="JLPAWIQBCTRZYDSKEGFXHUONVM")
        == "WXXHL GHXW"
    )


def test_keyphrase():
    assert keyphrase("et tu, brute?", key="JULIUS CAESAR") == "SHHKU FKHS"


def test_vigenere():
    assert (
        vigenere("divert troops to east ridge", key="WHITE")
        == "ZPDXV PAZHS LZBHI WZBKM ZNM"
    )


@pytest.mark.parametrize(
    "plaintext, key, expected",
    [
        pytest.param(
            "meet me at hammersmith bridge tonight",
            "CHARLES",
            "GDDOG DRQAR KYGDH DNKPR DAMSO GUPGK ICQY",
            id="pad last space",
        ),
        pytest.param(
            "hide the gold in the tree stump",
            "PLAYFAIR EXAMPLE",
            "BMODZ BXDNA BEKUD MUIXM MOUVI F",
            id="no padding",
        ),
    ],
)
def test_playfair(plaintext, key, expected):
    assert playfair(plaintext, key=key) == expected
