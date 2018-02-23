import RPi.GPIO as GPIO
import dht11
import os
import json
import geojson
import time
import threading
import urllib
import urllib2
import requests

url = 'https://municipal.systems/v1/data?key=keyData'

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin = 14)
result = instance.read()

id = 'tempdemo1'
location = geojson.Point(-87.68724, 42.05673)

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)

    payload = {'temperature':result.temperature, 'humidity':result.humidity, 'location':location, 'id':id}

    r = requests.post(url, json=payload, params='response=false')
    r = status.code

else:
    print("Error: %d" % result.error_code)
    time.sleep(10)