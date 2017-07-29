#this demos the user profile operations with pygle
#corresponding curl command would be:
#curl -X GET -H 'Accept: application/json' -H 'Authorization: Basic base64-encoded-APINAME:APITOKEN' 'https://api.wigle.net/api/v2/profile/user'

from pygle import config, profile #importing config accesses api name and token in the config.py of pygle's site-packages directory

#this outputs a dictionary directly (because of pygle), so no json parsing required
user_info = profile.user()

#keys in dictionary are userid, email, donate, joindate, lastlogin, session, success

if user_info[u'success']:
	print 'Username: {a}\nEmail: {b}\nDonating: {c}\nJoined: {d}\nLast Login: {e}\n'\
			.format(a = user_info[u'userid'], b = user_info[u'email'], c = user_info[u'donate'],\
			d = user_info[u'joindate'], e = user_info[u'lastlogin'])
else:
	print 'Sorry, was not able to pull user information from wigle.'

