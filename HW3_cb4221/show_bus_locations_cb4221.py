## find MTA data here: http://bustime.mta.info/wiki/Developers/SIRIVehicleMonitoring

#import pylab as pl
import os
import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

#%pylab inline ## only works in jupyter notebooks
#pl.rc('font', size=15)
this_key = sys.argv[1]
this_bus = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + this_key + "&VehicleMonitoringDetailLevel=calls&LineRef=" + this_bus

#print url
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busline = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']
num_bus = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']

print('Bus Line : ', busline)
print('Number of Active Buses: ', num_bus)
for i in range(num_bus):
    print ("Bus %s is at latitude  %s and longitude %s" %(i+1, lat, long))
