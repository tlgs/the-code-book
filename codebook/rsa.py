import base64
import secrets


def _nonzero_random_bytes(n: int) -> bytes:
    values = [x.to_bytes(1, "big") for x in range(1, 256)]
    seq = [secrets.choice(values) for _ in range(n)]
    return b"".join(seq)


def _pkcs1v15(n: int, e: int, M: bytes) -> bytes:
    """RSAES-PKCS1-v1_5

    See <https://datatracker.ietf.org/doc/html/rfc8017#section-7.2>
    """
    k = (n.bit_length() - 1) // 8 + 1

    # Length checking
    if len(M) > k - 11:
        raise ValueError("message too long")

    # EME-PKCS1-v1_5 encoding
    PS = _nonzero_random_bytes(k - len(M) - 3)
    EM = b"\x00\x02" + PS + b"\x00" + M

    # RSA encryption
    m = int.from_bytes(EM, "big")
    c = pow(m, e, n)
    C = c.to_bytes(k, "big")

    return C


def rsa(plaintext: str, *, public_key: tuple[int, int]) -> str:
    message = bytes(plaintext, "utf-8")
    ciphertext = _pkcs1v15(*public_key, message)
    return base64.b64encode(ciphertext).decode()
