import os
import json
from geojson import LineString
import time
import threading
import urllib
import urllib2
import requests
         


url = 'https://municipal.systems/v1/data?key=keyData' #keyData= is your Data Source Key. Generate this on the Source Page.

         
os.system('clear') #clear the terminal (optional)
         
if __name__ == '__main__':
            while True:
              #It may take a second or two to get good data
         
              os.system('clear')
	     
              path = LineString([-74.047, 40.719])
              startedAt = '2018-01-22T09:45:00.000Z'
              endedAt = '2018-01-22T10:45:00.000Z'
              routeId = 'Downtown Emergency Vehicle Route 4'
              vehicleId = 'Snow Plow 10' 
              type = 'Snow Plow'
              id = 'Plow Trip Alpha'

              payload = {'path':path, 'startedAt':startedAt, 'endedAt':endedAt, 'routeId':routeId, 
              'vehicleId':vehicleId, 'type':type, 'id':id}

              r = requests.post(url, json=payload)
              print r.status_code #200 = successful http request. 400 = bad request; check your syntax.  500 = server error, check stae status page.  
         
              time.sleep(60) #loop is extra, only need once.
