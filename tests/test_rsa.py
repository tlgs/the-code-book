import base64

from cryptography.hazmat.primitives.asymmetric import rsa as ext_rsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

from codebook.rsa import rsa


def test_rsa():
    private_key = ext_rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
    )

    pub = private_key.public_key().public_numbers()

    message = "Clifford Cocks"
    b64_ciphertext = rsa(message, public_key=(pub.n, pub.e))

    plaintext = private_key.decrypt(base64.b64decode(b64_ciphertext), PKCS1v15())

    assert plaintext.decode("utf-8") == message
