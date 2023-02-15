#source: https://chaobin.github.io/2015/07/22/a-working-understanding-on-SSL-and-HTTPS-using-python/
import ssl
import urllib.parse
from OpenSSL import crypto # pip install pyopenssl

url = "https://www.acadiau.ca"
addr = urllib.parse.urlsplit(url).hostname
port = 443
cert = ssl.get_server_certificate((addr, port), ssl_version=2)

#print(cert)

#PKCS #12, key+X509 cert
certificate = crypto.load_certificate(crypto.FILETYPE_PEM, cert)

# The signer of the server's certificate
print("\nISSUER---------------------------")

issuer = certificate.get_issuer()
print(issuer.get_components())

# The company's business information
print("\nBUSINESS INFORMATION-------------")
print(issuer.get_components())

#
subject = certificate.get_subject()
components = dict(subject.get_components()) # convert to dict
print(components)

print("\n")
