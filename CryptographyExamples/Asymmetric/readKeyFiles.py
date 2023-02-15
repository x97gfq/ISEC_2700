# adapted from source https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

#open the private_key.pem file
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

#get the value of the private key, print() it.
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
print("\nprivate_key:\n" + str(pem))


#open the public_key.pem file
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

#get the value of the public key, print() it.
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print("\npublic_key:\n" + str(pem))