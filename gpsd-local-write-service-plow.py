#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012, modified by Chris Penalosa, January 2018.
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading
import json
import geojson
 
gpsd = None #seting the global variable
 
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
      #print gpsd.fix.longitude,', ',gpsd.fix.latitude,'  gpsd.fix.altitude
 
      os.system('clear')

      location = geojson.Point((gpsd.fix.longitude, gpsd.fix.latitude))
      speed = gpsd.speed
      heading = gpsd.heading
      routeId = 'Downtown Emergency Vehicle Route 4'
      manufactured = "2017"
      make = 'Ford'
      model = 'F-150'
      color = 'Oxford White'
      fuel = 'gas'
      transmission = 'automatic'
      cost = '45000'
      value = '37500'
      vin = '1HGCM12345A006789'
      license plate = '12345NJ' 
      type = 'Snow Plow'
      id = 'Plow'+ gpsd.utc 

      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'location    ' , gpsd.fix.longitude, gpsd.fix.latitude
      print 'speed       ' , gpsd.speed
      print 'heading     ' , gpsd.heading

      f = open('/home/pi/Desktop/write', 'a') #local
      value = location, speed, heading, id
      s = str(value)
      json.dump(value, f)
     
      time.sleep(10) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
