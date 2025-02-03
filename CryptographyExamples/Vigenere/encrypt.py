# Vigenere Cipher 
# based on source @ https://www.geeksforgeeks.org/vigenere-cipher/
  
#Choose a Keyword: Select a keyword that will be used to encrypt the message. For example, let's use "KEY".
#Repeat the Keyword: Repeat the keyword so that it matches the length of the plaintext. For example, if the plaintext is "HELLO", the repeated keyword would be "KEYKE".
#Encrypt the Message: For each letter in the plaintext, shift it by the number of positions indicated by the corresponding letter in the keyword. The shift is based on the position of the letter in the alphabet (A=0, B=1, ..., Z=25).

# This function generates the key in a cyclic manner until it's length isn't equal to the length of original text 
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
# This function returns the encrypted text generated with the help of the key 
def cipherText(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 

if __name__ == "__main__": 
    msg = "THISCLASSISTHEBEST"
    keyword = "LUIGI"     #"MARIO", "LINK", "PIKACHU", "SAMUS", "KIRBY", "FOX", "DONKEY KONG", "YOSHI", "LUIGI", "NESS"
    key = generateKey(msg, keyword) 
    cipher_text = cipherText(msg,key)
    print("Msg: " + msg)
    print("Key: " + key)
    print("Cipher: " + cipher_text)