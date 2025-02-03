#based on https://nitratine.net/blog/post/encryption-and-decryption-in-python/
import os
from cryptography.fernet import Fernet 

key = Fernet.generate_key() #generate a key

input_file = input('What file to encrypt? (*.txt): ')

fullpath = os.getcwd() + "\CryptographyExamples\\Fernet\\" + input_file
print("encrypting: " + fullpath)

output_file = fullpath.replace("txt","encrypted")

print("\nUsing key: " + key.decode("utf-8") + "\n") #encoded as a byte array, serialize as a UTF-8 string

with open(fullpath, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

print("Check folder for: " + output_file)