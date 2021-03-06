""""------------- CH2 HTTP & working with web ------------"""

from urllib.request import urlopen
import urllib.error

reponse = urlopen('http://www.debian.org')

"""
status possible :
	all : http://www.iana.org/assignments/http-status-				codes/http-status-codes.xhtml
"""

try:
	urlopen('http://www.ietf.org/rfc/rfc0.txt')
except urllib.error.HTTPError as e:
	print('status', e.code)
	print('reason', e.reason)
	print('url', e.url)
	print('headers', e.headers)

""" 
from urllib.request import Request
"""
headers = {'Accept-Language': 'fr'}
req = Request('http://www.debian.org', headers=headers)
"""
req = Request('http://www.debian.org')
req.add_header('Accept-Language', 'fr')
response = urlopen(req)
"""


""" compression du contenu
req = Request('http://www.debian.org')
req.add_header('Accept-Encoding', 'gzip')
response = urlopen(req)
response.getheader('Content-Encoding')
import gzip
content = gzip.decompress(response.read())
content.splitlines()[:5]
"""

""" pas de compression
req = Request('http://www.debian.org')
req.add_header('Accept-Encoding', 'indentity')
response = urlopen(req)
print(response.getheader('Content-Encoding'))
"""

""" compression avec preference(estimation par default = 1.0)
req = Request('http://www.debian.org')
encodings = 'gzip, deflate;q=0.8, identity;q=0.0'
req.add_header('Accept-Encoding', encodings)
response = urlopen(req)
response.getheader('Content-Encoding')
"""

"""
response = urlopen('http://www.python.org')
format, params = response.getheader('Content-Type').split(';')
print(params)
charset = params.split('=')[1]
print(charset)
response.read().decode(charset)
"""

""" simule un user agent
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')
response = urlopen(req)
req.get_header('User-agent')
"""

""" recuperer le cookie recu
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
cookie_jar = CookieJar()
opener = build_opener(HTTPCoookieProcessor(cookie_jar))
opener.open('http://www.github.com')

""" """ l'exploiter
cookies = list(cookie_jar)
cookies[0].name
cookies[0].value
----------------------------
cookies[0].domain
cookies[0].path
----------------------------
cookies[0].expires
import datetime
datetime.datetime.fromtimestamp(cookies[0].expires)
----------------------------
cookies[0].get_nonstandard_attr('HttpOnly')
cookies[0].secure // true = using https
"""

""" redirection
req = Request('http://www.gmail.com')
response = urlopen(req)
response.url   // redirected url
req.full_url // original url
req.redirect_dict
"""

""" parse url
from urllib.parse import urlparse
result = urlparse('http://www.python.com:8080/dev/peps')
result.scheme  (http / https)
result.netloc (network location)
result.path 
...
join base url and relative url to create a absolute url
from urllib.parse import urljoin
urljoin('http://www.debian.org', 'intro/about')
--> autre resultat
urljoin('http://www.debian.org/intro/', 'about') le path contien intro/about

urljoin('http://www.debian.org/intro', 'about') le path contien que about (remplace le dernier dans le path)

// forc� un path a le remplac� par le nouveau
urljoin('http://www.debian.org/intro/about', '/News')

// navig� dans le dir parent
urljoin('http://www.debian.org/intro/about/', '../News')
devien /intro/about

// relative url devien absolue
urljoin('http://www.debian.org/intro/about/', 'http://www.python.org')

// reconnaitre les query strings
urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')

//convertir(parsing it) un query a un dictionaire
from urllib.parse import parse_qs
result = urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')
parse_qs(result.query)
chaque parametre (q, area,...) peux contenir 1 ou plusieur

// url encodings
from urllib.parse import quote
quote('A duck?')
%.. ascii hex code = escape sequences

//form� un url
1- encode path

path = 'pypi'
path_enc = quote(path)

2- encode query string (encode un dict)

from urllib.parse import urlencode
query_dict = { ':action': 'search', 'term': 'Are you quite sure this is a cheese shop?' }
query_enc = urlencode(query_dict)

3- combin� les 2
from urllib.parse import urlunparse
netloc = 'pypi.python.org'
// inverse de urlparse
urlunparse(('http', netloc, path_enc, '', query_enc, ''))
resultat = 'http://pypi.python.org/pypi?%3Aaction=search&term=Are+you+quite+sure +this+is+a+cheese+shop%3F'

// quand le '/' represente une part dans le path, en doit 'escape' individuelement ex:
username = '+Zoot/Dingo+'
user_encoded = quote(username, safe='') 
// safe='' ne pas ignorer le '/'
path = '/'.join(('', 'images', 'users', username))
"""

""" HTTP Methode
GET, HEAD, POST, OPTION, PUT, DELETE, TRACE, CONNECT, PATCH

req = Request('http://www.google.com', method='HEAD')
response = urlopen(req)
response.statis
response.read() // vide si ya pas de redirect au lien

//POST
data_dict = {'p' : 'Python'}
data = urlencode(data_dict).encode('utf-8')
req = Request('http://search.debian.org/cgi-bin/omega', data=data)
req.add_header('Content-Type', 'application/x-www-form-urlencode;charset=UTF-8')
response = urlopen(req) 
"""

