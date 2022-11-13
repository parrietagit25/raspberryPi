import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

Trigger = 10
Echo = 12

GPIO.setup(Trigger,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

print("Sensor Ultrasonico")

try:
	while True:
		GPIO.output(Trigger, False)
		time.sleep(0.5)
		
		GPIO.output(Trigger,True)
		time.sleep(0.00001)
		GPIO.output(Trigger,False)
		inicio=time.time()
		
		while GPIO.input(Echo) ==0:
			inicio = time.time()
			
		while GPIO.input(Echo) ==1:
			final = time.time()
		
		t_transcurrido = final-inicio
		
		distancia = t_transcurrido*34000
		
		distancia = distancia/2
		
		print("Distancia: {dist} CM".format(dist=distancia))
		
except KeyboardInterrupt:
	GPIO.cleanup()
