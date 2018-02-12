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
              speed = gpsd.fix.speed/1000
              heading = gpsd.fix.track
              manufacturer = 'DJI'
              operators = array('FCC', 'PAN NJ', 'Amazon')
              active = false
              model = 'Mavic Pro'
              color = 'Gray'
              type = 'UAV Drone'
              tripId = 'Amazon Delivery'+ gpsd.utc

         	
              print
              print ' GPS reading'
              print '----------------------------------------'
              print 'location    ' , round(gpsd.fix.longitude, 5), round(gpsd.fix.latitude, 5)
              print 'speed       ' , gpsd.fix.speed
              print 'heading     ' , gpsd.fix.track


              payload = {'location':location, 'speed':speed, 'heading':heading, 'manufacturer':manufacturer, 'operators':operators, 'active':active, 'model':model, 'color':color, 'type':type, 'tripId':tripId}

              r = requests.post(url, json=payload)
              print r.status_code #200 = successful http request. 400 = bad request; check your syntax.  500 = server error, check stae status page.  
         
              time.sleep(10) #default value will send GPS data every 10 seconds. use faster speeds for faster or right-of-way vehicles.
         
          except (KeyboardInterrupt, SystemExit): #press ctrl+c to stop the program
            print "\nStopping GPS program..."
            gpsp.running = False
            gpsp.join() # wait for the thread to finish what it's doing
          print "Done.\nExiting."
