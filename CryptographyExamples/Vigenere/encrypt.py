# Vigenere Cipher 
# based on source @ https://www.geeksforgeeks.org/vigenere-cipher/
  
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
    msg = "DARCYBENOITISTHEBEST"
    keyword = "RED"
    key = generateKey(msg, keyword) 
    cipher_text = cipherText(msg,key)
    print("Msg: " + msg)
    print("Key: " + key)
    print("Cipher: " + cipher_text)