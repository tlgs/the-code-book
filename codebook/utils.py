import functools
import inspect
import string


def validate(func):
    sig = inspect.signature(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)

        if (
            "plaintext" in bound.arguments
            and not bound.arguments["plaintext"].islower()
        ):
            raise ValueError("Plaintext should be lowercase.")

        elif "key" in bound.arguments and not bound.arguments["key"].isupper():
            raise ValueError("Key should be uppercase.")

        elif "cipher_alphabet" in bound.arguments and not set(
            bound.arguments["cipher_alphabet"]
        ) == set(string.ascii_uppercase):
            raise ValueError(
                "Cipher alphabet should be uppercase and contain all 26 letters."
            )

        return func(*args, **kwargs)

    return wrapper
