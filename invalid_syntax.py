"""R11-22 Real RSA call, then a SyntaxError later in the file."""
from cryptography.hazmat.primitives.asymmetric import rsa
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

def broken(:              # <-- SyntaxError on purpose
    return key
