#this shows the basic "search" function using pygle and dumps to screen

from pygle import config, network #importing config accesses api name and token in the config.py of pygle's site-packages directory

#just a test
my_ssid = 'prettyflyforawifi'

#Options are:
#onlymine (true or false, bool)
#first (designated offset of the first record you want, long int)
#latrange1, latrange2, longrange1, longrange2 (double)
#lastupdt (last updated timeyyyyMMdd[hhmm[ss]])
#netid (bssid, string)
#ssid (ssid of net, string)
#ssidlike (useful, allows sql wildcards, "%" and "_", string)
#variance (double, between 0.001 and 0.2, how tightly to stick to lat/long ranges)
#resultsPerPage (defaults to 100 for pygle, max 1000 per query, long)

net_results = network.search (ssid = my_ssid, first = 0, latrange1 = 30.0, latrange2 = 50.0,\
								longrange1 = -85.0, longrange2 = -120.0)

#print out some of the important bits
for result in net_results[u'results']:
	print result[u'ssid'], result[u'netid'], result[u'trilat'], result[u'trilong'], result[u'lastupdt']
