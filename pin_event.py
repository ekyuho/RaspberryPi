import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def gotit(channel):
  print("got it", channel)

GPIO.add_event_detect(26, GPIO.RISING, callback=gotit, bouncetime=300)

while True:
  v = GPIO.input(26)
  print(v)
  time.sleep(30)

GPIO.cleanup()
