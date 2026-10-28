"""R11-29 Homoglyph decoy identifier + a real RSA call."""
rsа = type("x", (), {})()  # Cyrillic a - not the rsa module
from cryptography.hazmat.primitives.asymmetric import rsa as _real
key = _real.generate_private_key(public_exponent=65537, key_size=2048)
