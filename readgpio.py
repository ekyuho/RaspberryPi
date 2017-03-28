import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)

while True:
  v = GPIO.input(26)
  print(v)
  time.sleep(0.1)
