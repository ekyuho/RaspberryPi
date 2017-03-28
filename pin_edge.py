import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  GPIO.wait_for_edge(26, GPIO.RISING)
  print("rising up")
