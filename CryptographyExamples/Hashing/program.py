import hashlib

m = hashlib.sha256()
m.update(b"The quick red fox jumps over the lazy brown dog")

hashvalue = m.hexdigest()
hashsize = m.digest_size
hashblock = m.block_size

print("\nhashvalue: {0}\nhashsize: {1}\nhashblock: {2}\n".format(hashvalue, hashsize, hashblock))
