#source: https://www.pythoncentral.io/hashing-files-with-python/
import hashlib
import os 

BLOCKSIZE = 65536
#hasher = hashlib.sha1()
hasher = hashlib.sha256()

target = input('What file to hash (SHA)?: ')
fullpath = os.getcwd() + "\CryptographyExamples\\Hashing\\" + target
print("Using " + fullpath)

with open(target, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)

print(hasher.hexdigest())