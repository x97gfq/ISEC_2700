#source: https://www.vitoshacademy.com/hashing-passwords-in-python/
import hashlib
import os
import binascii

#Verify a stored password against one provided by user
def verify_password(stored_password, provided_password):
    salt = stored_password[:64] #the salt is the first 64 characters
    stored_password = stored_password[64:] 
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


#hash a password
pwdToVerify = 'NovaScotiaCommunityCollege!'
stored_password = "b55e37018dc24220a85d726f3b215d2676db269be0d635cd2400b37812b5894ba945ac6f14c1afb460e3cd78f72be142cc93a8de18bcf8c82df9c70088f6fabdae21fb346e4904a2dfe99d795d6dc18bbebdc91731f3fa8028aafdfaa280fc57"

#verify the password
print("\n\nVerify Password: " + str(verify_password(stored_password, pwdToVerify)))

##negative test (bad password)
#bad_pwd = 'BadPassword2020!'
#print("\n\nVerify Password (negative test) '" + bad_pwd + "': " + str(verify_password(stored_password, bad_pwd)) + "\n\n")
