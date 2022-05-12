import RPi.GPIO as GPIO
import time

def button_callback(channel):
  print("!@#!@#!@#")

button_pin = 15

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
  time.sleep(0.1)
