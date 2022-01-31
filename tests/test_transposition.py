import pytest

from codebook.transposition import adfgvx, rail_fence, scytale


@pytest.mark.parametrize(
    "plaintext, n, expected",
    [
        pytest.param(
            "thy secret is thy prisoner; if thou let it go, thou art a prisoner to it",
            2,
            "TYERTSHPIOEITOLTTOHURARSNROTHSCEITYRSNRFHUEIGTOATPIOETI",
            id="n=2",
        ),
        pytest.param(
            "we are discovered. run at once.", 3, "WECRUOERDSOEERNTNEAIVDAC", id="n=3"
        ),
        pytest.param(
            "we are discovered. run at once.", 6, "WVOEOETNACRACRSENEEIDUDR", id="n=6"
        ),
    ],
)
def test_rail_fence(plaintext, n, expected):
    assert rail_fence(plaintext, n=n) == expected


@pytest.mark.parametrize(
    "plaintext, diameter, expected",
    [
        pytest.param(
            "send more troops to southern flank and",
            4,
            "STSFEROLNOUADOTNMPHKOSEARTRNEOND",
            id="mod=0",
        ),
        pytest.param(
            "we are discovered. flee at once.",
            3,
            "WOEEVEAEARRTEEODDNIFCSLEC",
            id="mod=1",
        ),
    ],
)
def test_scytale(plaintext, diameter, expected):
    assert scytale(plaintext, diameter=diameter) == expected


def test_adfgvx():
    assert (
        adfgvx("attack at 10 pm", key="MARK")
        == "V D G V V D D V D D G X D D F D A A D D F D X G"
    )
