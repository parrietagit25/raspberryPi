import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

arrGPIO = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

for x in arrGPIO:
	GPIO.setup(x, GPIO.OUT)
	GPIO.output(x, GPIO.HIGH)
	print("GPIO N#: {x} ON".format(x=x))
	time.sleep(1)

time.sleep(3)

for x in arrGPIO:
	GPIO.cleanup(x)
	print("GPIO N#: {x} OFF".format(x=x))
	time.sleep(1)
