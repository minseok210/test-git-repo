import RPI.GPIO as GPIO
import time

lesd_pin = 4
GPIO.setwarnings(false)

GPIO.setmode(GPIO.BCM)

GPIO.setmode(led_pin, GPIO.OUT)

for iin range(10):
  GPIO.output(led_pin,1)
  time.sleep(1)
  GPIO.output(led_pin,0)
  time.sleep(1)
GPIO.cleanup()
