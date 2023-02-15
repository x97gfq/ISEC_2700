#source: https://www.pythoncentral.io/hashing-files-with-python/
import hashlib

BLOCKSIZE = 65536
hasher = hashlib.sha1()

target = input('What file to hash (SHA)?: ')

with open(target, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)

print(hasher.hexdigest())