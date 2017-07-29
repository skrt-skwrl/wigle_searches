#take an input and produce bounding box using Nominatim from OpenStreetMap
#this makes a kml file with the box in a transparent red color

from geopy.geocoders import Nominatim
import sys, simplekml


geolocator = Nominatim()

#take named location directly from command line
#command form  is "python bb_nominatim.py "New York City" or...
#"python bb_nominatim.py "Brazil"

loc_name = sys.argv[1]
location = geolocator.geocode(loc_name)

#get bounding_box (geo_box) from location.raw
#this gives [South Latitude, North Latitude, West Longitude, East Longitude]
#for other things we need two corner points (SLat, WLong, NLat, ELong)

geo_box = location.raw[u'boundingbox']

#print to test it
print location

#output to kml to test it

kml = simplekml.Kml()
b_box = kml.newgroundoverlay (name=loc_name)
b_box.color = '371400FF' #this is transparent red
b_box.latlonbox.north = float(geo_box[1])
b_box.latlonbox.south = float(geo_box[0])
b_box.latlonbox.east = float(geo_box[3])
b_box.latlonbox.west = float(geo_box[2])

#save kml file with name based on the full location name
kml.save (str(location).replace(', ', '-').replace(' ', '_') + '_bounding_box.kml')
