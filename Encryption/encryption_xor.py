#source: https://en.wikipedia.org/wiki/XOR_cipher
from os import urandom


def genkey(length: int) -> bytes:
    """Generate key."""
    return urandom(length)


def xor_strings(s, t) -> bytes:
    """Concate xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode('utf8')
    else:
        # Bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])


#https://stackoverflow.com/questions/26802581/can-anyone-identify-this-encoding
#This is binary data held in a Python bytes object. Loosely, bytes that map to 
# printable ASCII characters are presented as those ASCII characters. All other 
# bytes are encoded \x** where ** is the hex representation of the byte.

message = 'This is a secret message'
print('Message:', message)

key = genkey(len(message))
print('Key:', key)

cipherText = xor_strings(message.encode('utf8'), key)
print('cipherText:', cipherText)

#decode it
print('decrypted:', xor_strings(cipherText, key).decode('utf8'))

# Verify
if xor_strings(cipherText, key).decode('utf8') == message:
    print('Unit test passed')
else:
    print('Unit test failed')
