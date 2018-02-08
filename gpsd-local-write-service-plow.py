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

      location = geojson.Point((round(gpsd.fix.longitude, 3), round(gpsd.fix.latitude, 3)))
      speed = gpsd.fix.speed/1000
      heading = gpsd.fix.track
      routeId = 'Downtown Emergency Vehicle Route 4'
      manufacturedAt = "2017-01-01"
      manufacturer = 'Ford'
      model = 'F-150'
      color = 'Oxford White'
      fuel = 'gas'
      transmission = 'automatic'
      cost = 45000
      value = 37500
      vin = '1HGCM12345A006789'
      plate = '12345NJ' 
      type = 'Snow Plow'
      id = 'Plow'+ gpsd.utc 

      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'location    ' , round(gpsd.fix.longitude, 3), round(gpsd.fix.latitude, 3)
      print 'speed       ' , gpsd.fix.speed/1000
      print 'heading     ' , gpsd.fix.track

      f = open('/home/pi/Desktop/write.json', 'a') #local
      data = {'location': location, 'speed':speed, 'heading':heading, 'routeId':routeId, 'manufacturedAt':manufacturedAt, 'manufacturer':manufacturer, 'model':model, 'color':color, 'fuel':fuel, 'transmission':transmission, 'cost':cost, 'value':value, 'vin':vin, 'plate':plate, 'type':type, 'id':id,}
      json.dump(data, f)
     
      time.sleep(10) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
