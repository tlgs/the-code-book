import pytest

from codebook.transposition import adfgvx, rail_fence, scytale


@pytest.mark.parametrize(
    "plaintext, n, expected",
    [
        pytest.param(
            "thy secret is thy prisoner; if thou let it go, thou art a prisoner to it",
            2,
            "TYERT SHPIO EITOL TTOHU RARSN ROTHS CEITY RSNRF HUEIG TOATP IOETI",
            id="n=2",
        ),
        pytest.param(
            "we are discovered. run at once.",
            3,
            "WECRU OERDS OEERN TNEAI VDAC",
            id="n=3",
        ),
        pytest.param(
            "we are discovered. run at once.",
            6,
            "WVOEO ETNAC RACRS ENEEI DUDR",
            id="n=6",
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
            "STSFE ROLNO UADOT NMPHK OSEAR TRNEO ND",
            id="mod=0",
        ),
        pytest.param(
            "we are discovered. flee at once.",
            3,
            "WOEEV EAEAR RTEEO DDNIF CSLEC",
            id="mod=1",
        ),
    ],
)
def test_scytale(plaintext, diameter, expected):
    assert scytale(plaintext, diameter=diameter) == expected


def test_adfgvx():
    assert adfgvx("attack at 10 pm", key="MARK") == "VDGVV DDVDD GXDDF DAADD FDXG"
