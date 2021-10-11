from codebook.transposition import rail_fence, scytale


def test_rail_fence():
    test_input = (
        "THY SECRET IS THY PRISONER; IF THOU LET IT GO, THOU ART A PRISONER TO IT"
    )
    expected = "TYERTSHPIOEITOLTTOHURARSNROTHSCEITYRSNRFHUEIGTOATPIOETI"
    assert rail_fence(test_input, rails=2) == expected


def test_scytale():
    test_input = "Send more troops to southern flank and"
    expected = "STSFEROLNOUADOTNMPHKOSEARTRNEOND"
    assert scytale(test_input, diameter=4) == expected
