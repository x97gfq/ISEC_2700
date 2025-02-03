#based on source @ https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_encryption_of_transposition_cipher.htm

#A transposition cipher is a method of encryption where the positions of the characters 
#in the plaintext are shifted according to a certain system, creating the ciphertext. Unlike 
#substitution ciphers, which replace characters with other characters, transposition ciphers 
#rearrange the characters.

#Key Points:
#Rearrangement: Characters are shuffled based on a specific algorithm or key.
#Same Characters: The ciphertext contains the same characters as the plaintext, just in a different order.
#Examples: Columnar transposition, Rail Fence cipher.
#Transposition ciphers are often combined with other types of ciphers to enhance security.

def main():
   myMessage = 'This is the message to encrypt'
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