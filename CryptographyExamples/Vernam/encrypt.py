#https://en.wikipedia.org/wiki/Baudot_code
#based on source @ https://repl.it/@GeorgeHill1/Vernam-Cipher

#The Vernam cipher, also known as the one-time pad, encrypts each character 
#of the plaintext with a corresponding character from a key of the same length

#The Vernam cipher can work with the Baudot code by treating each Baudot-encoded character as a binary string. Here's a step-by-step explanation:
#Convert Plaintext to Baudot Code: Each character in the plaintext is converted to its corresponding Baudot code. For example, "HELLO" would be converted to "11010 01000 11011 11011 11100".
#Generate a Key: Create a random key of the same length as the Baudot-encoded plaintext. For example, if the plaintext in Baudot code is "11010 01000 11011 11011 11100", the key might be "10101 11100 00011 10101 01010".
#XOR Operation: Perform an XOR operation between each bit of the Baudot-encoded plaintext and the corresponding bit of the key. The XOR operation is defined as:

import random, datetime

baudot = {
  'A': "10000",  'B': "00110",  'C': "10110",  'D': "11110",  'E': "01000",  '\'': "11000",  'F': "01110",  'G': "01010",  'H': "11010",
  'I': "01100",  'J': "10010",  'K': "10011",  'L': "11011",  'M': "01011",  'N': "01111",  'O': "11100",  'P': "11111",  'Q': "10111",
  'R': "00111",  'S': "00101",  'T': "10101",  'U': "10100",  'V': "11101",  'W': "01101",  'X': "01001",  'Y': "00100",  'Z': "11001",
  '*': "00011",  ',': "10001",  '.': "00010",  '_': "00001",  '/': "00000"
}

reverseBaudot = {v:k for k, v in baudot.items()}

def vernam(plaintext):
  plaintext = plaintext.upper()
  plaintext = plaintext.replace(' ', '_')
  key = ""
  for i in plaintext:
    random.seed(datetime.datetime.now())
    key += chr(65 + random.choice(range(0, 25)))
  print("Key   :\t", key)
  return encrypt(plaintext, key)

def encrypt(plaintext, key):
  plaincode = getBaudot(plaintext)
  keycode = getBaudot(key)
  xor = int(plaincode, 2) ^ int(keycode, 2)
  return getText(bin(xor)[2:].zfill(len(plaincode)))

def getBaudot(text):
  ret = ""
  for c in text:
    ret += baudot[c]
  return ret
  
def getText(baudotCode):
  splitBaudot = [baudotCode[i:i+5] for i in range(0, len(baudotCode), 5)]
  ret = ""
  for i in splitBaudot:
    ret += reverseBaudot[i]
  return ret


if __name__ == "__main__": 

    msg = "TESTING_THIS"

    #cipher = vernam(msg)
    #print("\nCipher (w/random key): " + cipher + "\n")

    key = "AAAAAAAAAAAA"
    cipher = encrypt(msg, key)
    print("Cipher (encrypted w/key: " + key + "): " + cipher + "\n")


    key_to_decrypt = ""
    cipher_to_decrypt = ""
    decrypted = encrypt(cipher_to_decrypt, key_to_decrypt)
    print("Cipher " + cipher + " (decrypted w/key: " + key + "): " + decrypted + "\n")

    #brute force attack:
    #possibleKeys = ["MARIO", "LINK", "PIKACHU", "SAMUS", "KIRBY", "FOX", "DONKEY KONG", "YOSHI", "LUIGI", "NESS"]
    #for x in range(len(possibleKeys)):
    #    key = possibleKeys[x]
    #    cipher = "MYFB_QMKZVN/.GHR/V"
    #    print("Possible Original/Decrypted Text:" + encrypt(cipher, key))
