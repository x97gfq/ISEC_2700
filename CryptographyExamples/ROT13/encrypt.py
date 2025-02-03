#ROT13 (rotate by 13 places) is a simple substitution cipher used to encode text. 
#It works by shifting each letter of the alphabet by 13 places. For example, 
#'A' becomes 'N', 'B' becomes 'O', and so on. Since the alphabet has 26 letters, 
#applying ROT13 twice returns the original text.

rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

# Function to translate plain text
def rot13(text):
   return text.translate(rot13trans)

def main():
   txt = "This is the message to encrypt"
   print(rot13(txt))
	
if __name__ == "__main__":
   main()