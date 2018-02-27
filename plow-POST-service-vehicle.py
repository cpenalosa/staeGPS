import os
from gps import *
from time import *
import json
import geojson
import time
import threading
import urllib
import urllib2
import requests
         
gpsd = None #seting the global variable


url = 'https://municipal.systems/v1/data?key=keyData' #keyData= is your Data Source Key. Generate this on the Source Page.
         
os.system('clear') #clear the terminal (optional)
         
class GpsPoller(threading.Thread):
          def __init__(self):
            threading.Thread.__init__(self)
            global gpsd #bring it in scope
            gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
            self.current_value = None
            self.running = True #setting the thread running to true
         
          def run(self):
            global gpsd
            while gpsp.running:
              gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
         
if __name__ == '__main__':
          gpsp = GpsPoller() # create the thread
          try:
            gpsp.start() # start it up
            while True:
              #It may take a second or two to get good data
         
              os.system('clear')
	     
              location = geojson.Point((round(gpsd.fix.longitude, 5), round(gpsd.fix.latitude, 5)))
              speed = round(gpsd.fix.speed/1000, 3)
              heading = gpsd.fix.track
              routeId = 'Downtown Emergency Vehicle Route 4'
              manufacturedAt = '2017-01-01' #Use ISO 8601 syntax YYYY-MM-DD 
              manufacturer = 'Ford'
              model = 'F-150'
              color = 'Oxford White'
              fuel = 'gas'
              transmission = 'automatic'
              cost = 45000
              value = 42000
              vin = '1HGCM12345A006789'
              plate = '12345NJ' 
              type = 'Snow Plow'
              id = 'Plow'+ gpsd.utc

         	
              print
              print ' GPS reading'
              print '----------------------------------------'
              print 'location    ' , round(gpsd.fix.longitude, 5), round(gpsd.fix.latitude, 5)
              print 'speed       ' , gpsd.fix.speed
              print 'heading     ' , gpsd.fix.track


              payload = {'location':location, 'speed':speed, 'heading':heading, 'routeId':routeId, 'id':id}


              r = requests.post(url, json=payload, params='response=false') #passing response=false in the query to save on data costs.
              print r.status_code #2xx = successful http request. 4xx = bad request; check your syntax/key.  5xx = server error, check stae status page.
              

         
              time.sleep(10) #default value will send GPS data every 10 seconds. use faster speeds for faster or right-of-way vehicles.
         
          except (KeyboardInterrupt, SystemExit): #press ctrl+c to stop the program
            print "\nStopping GPS program..."
            gpsp.running = False
            gpsp.join() # wait for the thread to finish what it's doing
          print "Done.\nExiting."
