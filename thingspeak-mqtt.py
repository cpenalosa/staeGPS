import paho.mqtt.publish as publish
import psutil
import string
import random
import os
from gps import *
from time import *
import time
import threading
import urllib
import urllib2

string.alphanum='1234567890avcdefghijklmnopqrstuvwxyzxABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "401537"

# The Write API Key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
writeAPIKey = "RVTEHDIE9BAU5EON"

# The Hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any Username.
mqttUsername = "penalosa619"

# Your MQTT API Key from Account > My Profile.
mqttAPIKey = "HRCK5SCU6WN8VGX9"

# Set the transport mode to WebSockets.
tTransport = "websockets"
tPort = 80

# Create the topic string.
topic = "channels/" + channelID + "/publish/" + writeAPIKey

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
      os.system('clear')

      lat = gpsd.fix.latitude
      lon = gpsd.fix.longitude
      altitude = gpsd.fix.altitude
      utc = gpsd.utc

      print
      print ' GPS reading'
      print '----------------------------------------'
      print 'longitude   ' , lon
      print 'latitude    ' , lat
      print 'altitude (m)' , altitude
      print 'time        ' , utc

      userdata = {"latitude": lat, 
                "longitude": lon, 
                "altitude": altitude, }
      payload = "field1=" + str(lon) + "&field2=" + str(lat) + "&field3=" + str(altitude)
      publish.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
      f = open('/home/pi/Desktop/write.json', 'a') #local
      value = gpsd.fix.longitude, gpsd.fix.latitude, gpsd.fix.altitude, gpsd.utc
      s = str(value)
      json.dump(value, f)
      time.sleep(5)
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
  print "Done\nExiting."
