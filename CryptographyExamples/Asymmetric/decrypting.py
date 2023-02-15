# adapted from source https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

#put encrypted byte string here:
encrypted = b'KgzZZRl5YJ60UQKapjGyYH/u2q3RdmrdnFgc+Epwgr3FtgLFl5EcHrXbA38j3cXV17EAiFPHDTCfQisXmIyy9GP1ja/+c/tLlSxkMWXciNyu1o49005rI5otqpxuisiA6jAUBhJ708BU4jYjCjk361hI6xriN5wDajG0zWL/nHEb/VU2iiywWW94sAriWTCnJiCVZuqaAdsFwD8HU78XE2zKFP/yNCBxhJWPDsfwrR/ywCap7d5g6cfghZKuaKOk13m4cEfkiQFLXwU6nYl6Z9cbLWVxWcm7zm73esNP9vMjBHIdNhbQx/j5WxIWyuT58tBdx3C0ouMVaoNs83DCzg=='

#open the private_key.pem file
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

original_message = private_key.decrypt(
    base64.b64decode(encrypted),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(original_message)