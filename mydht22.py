import sys
from time import sleep
import Adafruit_DHT
import requests

myAPI = "0D0HNYXTWO10M27Q"

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
           url = baseURL + "&field2=%s&field1=%s" % (RH, T)
           print(url)
           r = requests.get(url)
           print(r.text)
           sleep(20) #uploads DHT22 sensor values every 5 minutes
       except:
           print('exiting.')
           break

# call main
if __name__ == '__main__':
   main()
