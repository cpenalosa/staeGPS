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

url = 'https://municipal.systems/v1/data?key=3fe5570d-e853-4d0a-aaf1-61fc1228bcbf' #keyData is your Data Source Key. Generate this on the Source Page.

         
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

              location = geojson.Point((-122.329250, 47.610561))
              type = 'Dockless Bike'
              active = 'True'
              operators = 'SDOT'
              heading = '175.42'
              speed = '4.5 KM/H'
              id = 'Pilot Bike 1'

         	
              print
              print ' GPS reading'
              print '----------------------------------------'
              print 'location    ' , location
              print 'speed       ' , speed
              print 'heading     ' , heading

              payload = {'location':location, 'speed':speed, 'heading':heading, 'type':type, 'operators':operators, 'id':id, 'active':active}

              r = requests.post(url, json=payload)
              print r.content #200 = successful http request. 400 = bad request; check your syntax.  500 = server error, check stae status page.
         
              time.sleep(10) #default value will send GPS data every 10 seconds. use faster speeds for faster or right-of-way vehicles.
         
          except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
            print "\nStopping GPS program..."
            gpsp.running = False
            gpsp.join() # wait for the thread to finish what it's doing
          print "Done.\nExiting."
