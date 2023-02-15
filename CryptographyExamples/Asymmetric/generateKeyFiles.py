# adapted from source https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


#Getting a Key
#To generate the two keys, we can call rsa.generate_private_key with some general parameters. 
# #The public key will be found in the object that holds the creation of the private key.
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()


#Storing Keys
#To store the keys in a file, they first need to be serialized and then written to a file. 
#To store the private key, we need to use the following:

pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key.pem', 'wb') as f:
    f.write(pem)

pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key.pem', 'wb') as f:
    f.write(pem)    