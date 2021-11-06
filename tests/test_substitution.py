from codebook.substitution import caesar, generic, keyphrase


def test_caesar():
    assert caesar("veni, vidi, vici", shift=3) == "YHQL, YLGL, YLFL"


def test_generic():
    assert (
        generic("et tu, brute?", cipher_alphabet="JLPAWIQBCTRZYDSKEGFXHUONVM")
        == "WX XH, LGHXW?"
    )


def test_keyphrase():
    assert keyphrase("et tu, brute?", key="JULIUS CAESAR") == "SH HK, UFKHS?"
