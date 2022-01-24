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


def test_playfair():
    assert (
        playfair("meet me at hammersmith bridge tonight", key="CHARLES")
        == "GD DO GD RQ AR KY GD HD NK PR DA MS OG UP GK IC QY"
    )
