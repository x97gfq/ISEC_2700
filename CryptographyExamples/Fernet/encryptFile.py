#based on https://nitratine.net/blog/post/encryption-and-decryption-in-python/
from cryptography.fernet import Fernet 

key = Fernet.generate_key() #generate a key

input_file = input('What file to encrypt? (*.txt): ')
output_file = input_file.replace("txt","encrypted")

print("\nUsing key: " + key.decode("utf-8") + "\n") #encoded as a byte array, serialize as a UTF-8 string

with open(input_file, 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

with open(output_file, 'wb') as f:
    f.write(encrypted)

print("Check folder for: " + output_file)