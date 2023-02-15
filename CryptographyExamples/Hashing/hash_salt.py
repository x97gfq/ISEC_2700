#source: https://www.vitoshacademy.com/hashing-passwords-in-python/
import hashlib
import os
import binascii

#Hash a password for storing
def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii') #joins together the hash with its salt (salt is first 64 characters)

#Verify a stored password against one provided by user
def verify_password(stored_password, provided_password):
    salt = stored_password[:64] #the salt is the first 64 characters
    stored_password = stored_password[64:] 
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


#hash a password
pwd = 'JodreySchoolOfComputerSciecne2020!'
stored_password = hash_password(pwd)
print("\n\nThe password '" + pwd + "' will be stored as: " + stored_password)

#then uncomment these lines and run the whole program
##verify the password
#print("\n\nVerify Password '" + pwd + "']: " + str(verify_password(stored_password, pwd)))

##negative test (bad password)
#bad_pwd = 'BadPassword2020!'
#print("\n\nVerify Password (negative test) '" + bad_pwd + "': " + str(verify_password(stored_password, bad_pwd)) + "\n\n")
