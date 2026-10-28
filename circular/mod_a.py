"""R11-31 Circular import A (has the RSA call)."""
from cryptography.hazmat.primitives.asymmetric import rsa
from circular import mod_b  # noqa: circular
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
