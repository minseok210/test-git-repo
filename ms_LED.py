import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, flag, rc):
	client.subscribe("MS_p")

def on_message(client, userdata, msg):
	if 2 in msg.payload:
		GPIO.output(11, True)
	else :
		GPIO.output(11, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


client.loop_forever()
