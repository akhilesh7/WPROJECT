#!/usr/bin/python2

import json
import urllib
from weather import Weather
weather = Weather()


serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
print "Hey hi.. Welcome to Akhibot \n"


while True:

        address = raw_input("\nEnter location:\n")
        if (address)<1: break

        url = serviceurl +  urllib.urlencode({'sensor':'false','address':address})
        #print 'Retrieving',url
        uh = urllib.urlopen(url)
        data = uh.read()
        #print 'Retrieved',len(data)

        try: 
		js=json.loads(str(data))
		location = weather.lookup_by_location(address)
		forecasts = location.forecast()
	
        except: js=None
        if 'status' not in js or js['status']!='OK':
                print '===Failed to retrieve==='
                #print data
                continue
	
        #print json.dumps(js, indent=4) 
      
        lat = js["results"][0]["geometry"]["location"]["lat"]
        lon = js["results"][0]["geometry"]["location"]["lng"] 
	print "Latitude: %s N" %(lat)
	print "Longitude: %s E" %(lon)
	#forecasts = location.forecast()
	i=1
	for forecast in forecasts:
		if i< 4:
			print "Weather in %s: %s" %(address,forecast.text())
			print (forecast.date())
			print "High:  %s "%(forecast.high()) + ' deg F' 
			print "Low:  %s"%(forecast.low()) + ' deg F' 
			i=i+1;	
 


