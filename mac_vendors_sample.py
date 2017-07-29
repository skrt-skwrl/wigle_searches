import urllib2

url = 'http://api.macvendors.com/'

mac = 'a0:63:91:55:6f:01'

vendor = urllib2.urlopen(url + mac).read()

# or in other words...
# vendor = urllib2.urlopen('http://api.macvendors.com/a0:63:91:55:6f:01').read()

print vendor

