# kyuho Kim, 2017-12-19
#
#  For DHT22 library, http://www.instructables.com/id/Raspberry-PI-and-DHT22-temperature-and-humidity-lo/
#  For ThingSpeak code, https://www.hackster.io/adamgarbo/raspberry-pi-2-iot-thingspeak-dht22-sensor-b208f4
#  In summary,
#   git clone https://github.com/adafruit/Adafruit_Python_DHT
#   cd Adafruit_Python_DHT
#    sudo python3  setup.py install  # for python3
#

"""
dht22.py

Temperature/Humidity monitor using Raspberry Pi and DHT22.
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in
Modified by Adam Garbo on December 1, 2016
"""

import sys
from time import sleep
import Adafruit_DHT
import requests

myAPI = "YOUR API KEY"

def getSensorData():
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 22) #22 refers to GPIO 22, or pin 15 on the RPi
   return ("%.0f"%(RH), "%.02f"%(T))

def main():
   print('starting...')
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

   while True:
       try:
           RH, T = getSensorData()
           print(T, RH)
           url = baseURL + "&field1=%s&field2=%s" % (RH, T)
           print(url)
           r = requests.get(url)
           print(r.text)
           sleep(300) #uploads DHT22 sensor values every 5 minutes
       except:
           print('exiting.')
           break

# call main
if __name__ == '__main__':
   main()
