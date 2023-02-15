#source: https://chaobin.github.io/2015/07/22/a-working-understanding-on-SSL-and-HTTPS-using-python/
import ssl
import urllib.parse
from OpenSSL import crypto # pip install pyopenssl

url = "https://www.acadiau.ca"
addr = urllib.parse.urlsplit(url).hostname
port = 443
cert = ssl.get_server_certificate((addr, port), ssl_version=2)

#print("CERTIFICATE-(PKCS #12, key+X509 cert)-------------------------")
#print(cert)
crtObj = crypto.load_certificate(crypto.FILETYPE_PEM, cert)

#get the public key from the certificate object
pubKeyObject = crtObj.get_pubkey()
pubKeyString = crypto.dump_publickey(crypto.FILETYPE_PEM,pubKeyObject)

print("PUBLIC_KEY (from certificate X509 object)---------------------")
print(pubKeyString)