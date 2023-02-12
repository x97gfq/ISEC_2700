#based on source @ https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_decryption_of_transposition_cipher.htm
import math

def main():
   myMessage= 'Tlsoha misaessw  ecis'
   myKey = 6
   plaintext = decryptMessage(myKey, myMessage)

   print("The plain text is: " + plaintext)


def decryptMessage(key, message):
   numOfColumns = math.ceil(len(message) / key)
   numOfRows = key
   numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
   plaintext = [''] * numOfColumns #array
   col = 0
   row = 0
   
   for symbol in message:
      plaintext[col] += symbol
      col += 1
      if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
         col = 0 
         row += 1 
   return ''.join(plaintext)

if __name__ == '__main__': #this runs the main() function when this file is run standalone
   main()