
from pygle import config, network 

my_bssid = '00:1E:52:F4:DD:73'
my_operator = 310410 #310 is USA, 410 is ATT/old cingular
my_lac = 7028 #lac in the state of Colorado
my_cid = 18523 #particular cell id in lac 7028


wifi = network.detail(netid = my_bssid)
gsm = network.detail(operator = my_operator, lac = my_lac, cid = my_cid)



wifi_record = wifi[u'results'][0]

print '\n----------------------------WiFi Record-------------------------------------------'
print wifi_record[u'netid'], wifi_record[u'ssid'], wifi_record[u'lastupdt'],\
		wifi_record[u'trilat'], wifi_record[u'trilong']
print '----------------------------------------------------------------------------------\n'

# now the individual observations
for result in wifi_record[u'locationData']:
	print result [u'ssid'], result[u'lastupdt'], result[u'latitude'],\
			result[u'longitude'], result[u'encryptionValue']
print '----------------------------------------------------------------------------------\n'


#print some data about the trilaterated gsm position
gsm_record = gsm[u'results'][0]

print '\n------------------------------GSM Record------------------------------------------\n'
print gsm_record[u'id'], gsm_record[u'lastupdt'], gsm_record[u'trilat'], gsm_record[u'trilong']
print '----------------------------------------------------------------------------------\n'

#now print the individual observations	
for result in gsm_record[u'locationData']:
	print result[u'lastupdt'], result[u'time'], result[u'latitude'], result[u'longitude']


