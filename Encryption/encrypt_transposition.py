#based on source @ https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_encryption_of_transposition_cipher.htm

def main():
   myMessage = 'This class is awesome'
   myKey = 6
   ciphertext = encryptMessage(myKey, myMessage)
   
   print("Cipher Text is: " + ciphertext)


def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        position = col
        while position < len(message):
            ciphertext[col] += message[position]
            position += key
    return ''.join(ciphertext) #Cipher text

if __name__ == '__main__':
   main()