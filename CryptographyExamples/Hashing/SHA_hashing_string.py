import hashlib

#Creating a SHA-256 Hash Object: 
#This initializes a new SHA-256 hash object.
m = hashlib.sha256()
#The update() method feeds the data (in bytes) into the hash object. 
#It is converted to bytes using the b prefix.
m.update(b"The quick red fox jumps over the lazy brown dog")

#The hexdigest() method returns the hash value as a hexadecimal string.
hashvalue = m.hexdigest()
#This returns the size of the resulting hash in bytes (32 bytes for SHA-256).
hashsize = m.digest_size
#This returns the internal block size of the hash algorithm (64 bytes for SHA-256).
hashblock = m.block_size

print("\nhashvalue: {0}\nhashsize: {1}\nhashblock: {2}\n".format(hashvalue, hashsize, hashblock))
