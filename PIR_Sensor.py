import RPi.GPIO as GPIO
import time
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #PIR motion sensor data
GPIO.setup(3, GPIO.OUT)         #LED pin
while True:
       i=GPIO.input(11)
       if i==1:
             print ("Motion: "+ str(datetime.datetime.now()))
             GPIO.output(3, 1)
             time.sleep(0.5)
       else:
             GPIO.output(3, 0)
             time.sleep(0.5)
