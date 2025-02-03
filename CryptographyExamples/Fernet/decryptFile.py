import os
from cryptography.fernet import Fernet 

input_file = input('What file to decrypt? (*.encrypted): ')
key = input('Key? ')
key = str.encode(key) #using your key from the encryption... (this is encoded as a byte array)

fullpath = os.getcwd() + "\CryptographyExamples\\Fernet\\" + input_file
print("decrypting: " + fullpath)

output_file = fullpath.replace("encrypted","decrypted")

print("\nUsing key: " + key.decode("utf-8") + "\n")

with open(fullpath, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

print("Check folder for: " + output_file)