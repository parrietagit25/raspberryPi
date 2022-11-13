from gpiozero import LED
from time import sleep

red = LED(17)

while True:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
    
"""
import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.OUT) 
GPIO.output(17, True)
print("Pasando por aca")
sleep(2)
print("off")
GPIO.output(17, False)
"""


