"""R11-26 Mixed tabs and spaces around a real EC call."""
from cryptography.hazmat.primitives.asymmetric import ec
def make():
	key = ec.generate_private_key(ec.SECP256R1())
        # space-indented comment
	return key
