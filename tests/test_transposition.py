from codebook.transposition import rail_fence, scytale


def test_rail_fence():
    assert (
        rail_fence(
            "thy secret is thy prisoner; if thou let it go, thou art a prisoner to it",
            rails=2,
        )
        == "TYERTSHPIOEITOLTTOHURARSNROTHSCEITYRSNRFHUEIGTOATPIOETI"
    )


def test_scytale():
    assert (
        scytale("send more troops to southern flank and", diameter=4)
        == "STSFEROLNOUADOTNMPHKOSEARTRNEOND"
    )
