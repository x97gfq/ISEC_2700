#source: https://www.pythoncentral.io/hashing-files-with-python/
import hashlib

BLOCKSIZE = 65536
hasher = hashlib.md5()

target = input('What file to hash (MD5)?: ')

with open(target, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)

print(hasher.hexdigest())