# adapted from source https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import os

#put encrypted byte string here:
encrypted = b'DmoxcKNnJOtugIwK7hBkGczZMz1ni+Uehe/7lB8fKh4QQhKOLvEzcEdmW4LVvbetyi3iGM8RtzTzUrXqL9SpY3c3t4mUI6auewgO4IE+XwsMudO1rMJQbUbUCLgByee1k0E1opXEWOEsKC7YEayXSjvDQe3nWpA79+GPggG42+xl7pkVZyug4Vz0ffQd9jLpsrg4hrymP1aPQmYkbmKh0NIm9sVAGz3UMOWIuZehMmND9bTQ0CwkH6gHMsQiYeL1U8VRZ9hB8dMJ52WEAfgcdExX9CMJX6L/4gGC38pPxH++TXTyphMJDHBVBxp+nVKLrTuBbaYa86ecvgglU6aYzw=='

#open the private_key.pem file
with open(os.getcwd() + "\CryptographyExamples\\Asymmetric\\private_key.pem", "rb") as key_file:
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