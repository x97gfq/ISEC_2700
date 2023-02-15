#source: https://chaobin.github.io/2015/07/22/a-working-understanding-on-SSL-and-HTTPS-using-python/
import ssl
import urllib.parse

url = "https://www.acadiau.ca"
addr = urllib.parse.urlsplit(url).hostname
port = 443
cert = ssl.get_server_certificate((addr, port), ssl_version=2)

print(cert)