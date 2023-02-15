#https://en.wikipedia.org/wiki/Baudot_code
#based on source @ https://repl.it/@GeorgeHill1/Vernam-Cipher

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

    msg = "WELCOMETOACADIAUNIVERSITY"

    cipher = vernam(msg)
    print("\nCipher (w/random key): " + cipher + "\n")

    key2 = "ANNAPOLISVALLEY"
    cipher2 = encrypt(msg, key2)
    print("Cipher2 (encrypted w/key: " + key2 + "): " + cipher2 + "\n")

    decrypted = encrypt(cipher2, key2)
    print("Cipher2 " + cipher2 + " (decrypted w/key: " + key2 + "): " + decrypted + "\n")

    #brute force attack:
    #possibleKeys = ["BIOLOGY", "CHEMISTRY", "COMPUTERSCIENCE", "MATH", "BUSINESS"]
    #for x in range(len(possibleKeys)):
    #    key = possibleKeys[x]
    #    cipher = "MYFB_QMKZVN/.GHR/V"
    #    print("Possible Original/Decrypted Text:" + encrypt(cipher, key))
