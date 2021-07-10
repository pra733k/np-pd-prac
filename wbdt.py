#     --------Coursera Using Python to Access Web Data Practice Codes--------------

# REgex Library to search  within strings
import re
yy="my first line with numbers 27 & 24"
x=re.findall('[0-9]+',yy)
print(x)



import re
yy="XYZ: Using : char"
x=re.findall('^X.+?:',yy)
print(x)



import re
yy="prateek@gmail.com is my email"
x=re.findall('\S+@+\S+',yy)
print(x)



import re
yy="From prateek@gmail.com Sat 0/00/0000 2000"
x=re.findall('^From (\S+@+\S+)',yy)
print(x)



import re
yy="From prateek@gmail.com Sat 0/00/0000 2000"
x=re.findall('(^From )\S+@+\S+',yy)
print(x)



import re
data="From prateek@gmail.com Sat 0/00/0000 2000"
atpos=data.find('@')
sppos=data.find(' ',atpos)
xx=data[atpos+1:sppos]
print(xx)



# Double Split Pattern
import re
yy="From prateek@gmail.com Sat 0/00/0000 2000"
words= yy.split()
email=words[1]
pieces=email.split('@')
print(pieces[1])



import re
yy="From prateek@gmail.com Sat 0/00/0000 2000"
words= yy.split()
print(words)
email=words[1]
print(email)
pieces=email.split('@')
print(pieces[0])



# fine tuning
import re
yy="From prateek@gmail.com Sat 0/00/0000 2000"
x=re.findall('@([^ ]*)',yy)
print(x)

# *************************************************

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()



import urllib
import re
from bs4 import BeautifulSoup
url = input('http://py4e-data.dr-chuck.net/comments_42.html')
html = urlib.request(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        sum=sum+i
print(sum)



# An HTTP Request in Python
import socket
mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if( len(data) < 1 ):
		break
	print(data.decode())
mysock.close()



import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()



# Reading Web Pages Using urllib in Python
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #file handle
for lines in fhand:
	print(lines.decode().strip())

from six.moves import urllib
temp_file, _ = urllib.request.urlretrieve('http://data.pr4e.org/romeo.txt')
print(temp_file)



# Reading  all the words in a file (basically on internet)
import urllib.request, urllib.parse, urllib.error
file_handle= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in file_handle:
	words = line.decode().split() #remove split to get count of each alphabet
	for word in  words:
		counts[word] = counts.get(word, 0) +1
print(counts)



# Web Scraping using bs4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as s
url = 'http://www.dr-chuck.com/page1.html'
html = urllib.request.urlopen(url).read()
soup = s(html,'html.parser')
tags = soup('a')
for tag in tags:
	print(tag.get('href', None))



# Worked example with bs4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = ''
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))



# Assignment 1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_776615.html'
html = urlopen(url, context=ctx).read()
page_soup = BeautifulSoup(html, "html.parser")
comment = page_soup.findAll("span",{"class":"comments"})
li=[]
for i in comment:
	x=i.get_text()
	y=int(x)
	li.append(y)
print(sum(li))



# Assignment 2
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Travis.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
x = tags[17].get('href', None)
for i in range(6):
	url = x
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	x = tags[17].get('href', None)
	y =x[39:]
	z = y.split('.')
	li =[]
	for n in z:
		li.append(n)
	print(li[0])
		




# Web Services with serialization formats-> XML & Json (formats of wire protocol)
# XML validation = xml document + xml schema contract


# PARSING XML
import xml.etree.ElementTree as ET
data = '''<person>   
			<name>Prateek</name>
			<phone type='intl'> 80555 </phone>
			<email hide='yes'/>
		  </person>'''  #''' quoted string is multi line string in py
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))



import xml.etree.ElementTree as ET
data = '''<stuff>
				<users>   
					<user x='2'>
						<id>001</id>
						<name>Chuck</name>
					</user>
					<user x='7'>
						<id>009</id>
						<name>Brent</name>
					</user>
		  		</users>
		  </stuff>'''
stuff = ET.fromstring(data)
a = stuff.findall('users/user')
print('User Count is :', len(a))
for i in a:
	print('Name', i.find('name').text)
	print('Id', i.find('id').text)
	print('Attribute', i.get('x'))



import xml.etree.ElementTree as ET
input = '''<stuff><users><user x="2"><id>001</id><name>Chuck</name></user><user x="7"><id>009</id><name>Brent</name></user></users></stuff>'''																																																																																																																																																																																																				
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))



# Assignment
# The program will prompt for a URL, read the XML data from that URL using urllib 
# and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url =  input('Enter location: ')
print('Retrieving', url)
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "lxml")
print('Retrieved', len(html), 'characters')
s = soup.findAll('count')
print('Count:', len(s))
li = []
for i in s:
	y = i.get_text()
	li.append(y)
x = map(int,li)
print('Sum:',sum(x))



# JSON - Method of Serialization
import json
data = '''{"name":"Prateek",
"phone":{"type":"intl","number":"10101"},
"email":{"hide":"yes"}}'''
info = json.loads(data)
print(info["name"])
print(info["email"]["hide"])



import json
input = '''[
{"id":"001", "name":"ABC"},
{"id":"009", "name":"XYZ"}]'''

info = json.loads(input)
print('User Count', len(info))
for item in info:
	print(item['name'])
	print(item['id'])



# GeoCoding - API of Google Maps
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('latitude:', lat, 'longitude:', lng)
    location = js['results'][0]['formatted_address']
    print("Formatted Address:", location)



# Assignment
# The program will prompt for a URL, read the JSON data from that URL using urllib 
# and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum
import json
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter location: ')
print('Retrieving', url)
html = urlopen(url, context=ctx).read()
print('Retrieved', len(html), 'characters')
js = json.loads(html)
x = js['comments']
print("Count:", len(x))
li=[]
for i in x:
	y = i['count']
	li.append(y)
print(sum(li))
	


# Gogle Maps API Assignment
import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    # print(json.dumps(js, indent=4))
    x = js['results'][0]['place_id']
    print('Place id', x)







# AWS
# EC2
# Instances
# Launch Instances
# take Linux AMI, SSD Vol type
# t3 micro in choose Instance type
# now configure -> change IAM role- EC2 Rekogniion-DD
# (or create) (IAM, Access Management, EC2 Rekognition)
# leave tags as it Is 
# select rules in configure security group
# go to security group to add new
# Review andlaunch
# proceede w/o a key  pair
# view Instances- name facial recognition