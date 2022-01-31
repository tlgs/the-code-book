import base64

import pytest
from cryptography.hazmat.primitives.asymmetric import rsa as ext_rsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15

from codebook.rsa import rsa


@pytest.fixture(scope="module")
def keys():
    private_key = ext_rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def test_rsa(keys):
    private_key, public_key = keys
    pub = public_key.public_numbers()

    message = "Clifford Cocks"
    b64_ciphertext = rsa(message, public_key=(pub.n, pub.e))

    plaintext = private_key.decrypt(base64.b64decode(b64_ciphertext), PKCS1v15())

    assert plaintext.decode() == message


def test_rsa_raises(keys):
    _, public_key = keys
    pub = public_key.public_numbers()

    message = """\
The upward creep of postal rates
accompanied by the deterioration
of postal service is a trend that
may or may not continue, but as far as
most private communication is con-
cerned, in a few decades it probably will
not matter. The reason is simple. The
transfer of information will probably be
much faster and much cheaper by "elec-
tronic mail" than by conventional postal
systems. Before long it should be possi-
ble to go to any telephone, insert a mes-
sage into an attachment and dial a num-
ber. The telephone at the other end will
print out the message at once.
"""

    with pytest.raises(ValueError):
        rsa(message, public_key=(pub.n, pub.e))
