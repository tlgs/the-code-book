"""
This module defines the RSA public-key algorithm.

The RSA cryptosystem involves multiple steps:
key generation, key distribution, encryption, and decryption.
This solution focuses solely on the **encryption** stage.

It implements the encryption operation using the PKCS1 v1.5 padding scheme.
"""
import base64
import secrets


def _pkcs1v15(n: int, e: int, M: bytes) -> bytes:
    """RSAES-PKCS1-V1_5 encryption operation

    - `n` is the public modulus
    - `e` is the public exponent
    - `M` is the message to be encrypted - an octet string

    See:
      - <https://datatracker.ietf.org/doc/html/rfc8017#section-7.2>
      - <https://stackoverflow.com/q/70910756/5818220>
    """
    k = (n.bit_length() - 1) // 8 + 1

    # Length checking
    if len(M) > k - 11:
        raise ValueError("message too long")

    # EME-PKCS1-v1_5 encoding
    PS = bytes(secrets.randbelow(255) + 1 for _ in range(k - len(M) - 3))
    EM = b"\x00\x02" + PS + b"\x00" + M

    # RSA encryption
    m = int.from_bytes(EM, "big")
    c = pow(m, e, n)
    C = c.to_bytes(k, "big")

    return C


def rsa(plaintext: str, *, public_key: tuple[int, int]) -> str:
    """RSA public-key algorithm (Appendix J, page 379)

    - `plaintext` is the message to be encrypted
    - `public_key` is the tuple `(n, e)` consisting of the public modulus and exponent

    Unlike the example in the book, practical applications of RSA require the
    usage of a padding scheme; this implementation employs the PKCS1 v1.5
    encryption operation as defined in RFC 8017.
    """
    message = bytes(plaintext, "utf-8")
    ciphertext = _pkcs1v15(*public_key, message)
    return base64.b64encode(ciphertext).decode()
