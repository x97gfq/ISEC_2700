from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Generate RSA keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()

# Message to be signed
message = b"A message I want to sign"

# Sign the message
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# WRITING OUT Message, Signature, and Keys

# write out the message
with open("signature/files/my_message.txt", 'wb') as file:
    file.write(message)

#write out the signature
with open("signature/files/my_signature.sig", 'wb') as file:
    file.write(signature)

#write out the public key

# Serialize the public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open("signature/files/my_public_key.pem", 'wb') as file:
    file.write(public_key_pem)

# write out the private key

# Serialize the private key to PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()  # No encryption for simplicity
)
with open("signature/files/my_private_key.pem", 'wb') as file:
    file.write(private_key_pem)

