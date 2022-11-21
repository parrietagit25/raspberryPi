#! /usr/bin/env python

from gpiozero import LED 
from time import sleep 

red = LED(17) 

red.on()    #turn led on 
sleep(0.5)    #delay for 1 second 
red.off()   #turn led off 
sleep(1)
