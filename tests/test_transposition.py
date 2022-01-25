from codebook.transposition import adfgvx, rail_fence, scytale


def test_rail_fence():
    assert (
        rail_fence(
            "thy secret is thy prisoner; if thou let it go, thou art a prisoner to it",
            n=2,
        )
        == "TYERTSHPIOEITOLTTOHURARSNROTHSCEITYRSNRFHUEIGTOATPIOETI"
    )


def test_scytale():
    assert (
        scytale("send more troops to southern flank and", diameter=4)
        == "STSFEROLNOUADOTNMPHKOSEARTRNEOND"
    )


def test_adfgvx():
    assert (
        adfgvx("attack at 10 pm", key="MARK")
        == "V D G V V D D V D D G X D D F D A A D D F D X G"
    )
