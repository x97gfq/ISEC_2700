#based on source @ https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
#reference: ASCII character chart @ http://www.asciitable.com/

def encrypt(text,s):
   result = ""
   # transverse the plain text
   for i in range(len(text)):
      char = text[i].upper()
      result += chr((ord(char) + s-65) % 26 + 65)  #uppercase A is the 65th character
   return result

#check the above function
text = "THIS IS THE MESSAGE TO ENCRYPT"
s = 4

c = encrypt(text,s)

print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Cipher: " + c)