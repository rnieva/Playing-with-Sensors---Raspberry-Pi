import RPi.GPIO
import time
import dht11

RPi.GPIO.setmode(RPi.GPIO.BCM)

#depend where you are connecting the data pin
instance = dht11.DHT11(pin = 4)

while True:
    result = instance.read()   #check the result from dht11 library
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
    time.sleep(3)
