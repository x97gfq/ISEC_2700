from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


# Read the PEM-encoded public key from the file
with open("signature/files/their_public_key.pem", 'rb') as file:
    pem_data = file.read()

# Load the public key
their_public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())


# Read the signed message from the file
with open("signature/files/their_message.txt", 'rb') as file:
    their_message = file.read()



# Read the signed message from the file
with open("signature/files/their_signature.sig", 'rb') as file:
    their_signature = file.read()


#their_message = b"sent me bitcoin!"

# Verify the signature
try:
    their_public_key.verify(
        their_signature,
        their_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except Exception as e:
    print("Signature is invalid:", e)

