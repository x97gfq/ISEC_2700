# Vigenere Cipher 
# based on source @ https://www.geeksforgeeks.org/vigenere-cipher/
  
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 

# This function decrypts the encrypted text and returns the original text 
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 


if __name__ == "__main__": 
    cipher = "UEUTCEVRRZXLJXKVFHJX"
    key = generateKey(cipher,"RED")
    print("Original/Decrypted Text:" + originalText(cipher, key))

    #brute force attack:
    #possibleKeys = ["RED", "GREEN", "BLUE"]
    #for x in range(len(possibleKeys)):
    #    ciphertext = "ENCRYPTEDMESSAGEHERE"
    #    key = generateKey(ciphertext, possibleKeys[x])
    #    print("Possible Original/Decrypted Text:" + originalText(ciphertext, key))