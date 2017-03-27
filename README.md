# Playing-with-Sensors---Raspberry-Pi
The goal of this repository is to show to user without any knowledge about sensors the easiest way to use them using a Raspberry Pi. Connect and Play. :)

------------------------------------------------------
<h2>Using a DS18B20 Temperature Sensor</h2>
Steps:

- 1- Download python and update if it's required
<p>sudo apt-get install python or python3
<p>sudo apt-get update
<p>sudo apt-get upgrade
<p>


- 2- Connect the sensor to Raspberry Pi

![alt tag](https://raw.github.com/rnieva/Playing-with-Sensors---Raspberry-Pi/master/scheme1_DS18B20.png)

[GPIO pins](https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-gpio-numbers.png)
<p>Sensor DS18B20 with cable
<p>Black --> GND
<p>Yellow --> GPIO 4 
<p>Red --> VDD 3.3v
<p>
<p>Sensor DS18B20 without cable
<p>From plane face:
<p>Left leg --> GND
<p>Center leg --> GPIO 4 
<p>Right leg --> VDD 3.3v
<p>


- 3- Edit config.txt
<p>sudo nano /boot/config.txt
<p>Add dtoverlay=w1-gpio on the bottom of the file 
<p>sudo reboot
<p>


- 4- Create Script 
<p>ls -l /sys/bus/w1/devices/ --> It show a list of the devices currently connected to your Raspberry Pi
<p>sudo nano test_sensor1.py --> Create a new python file
<p>Copy the code from (DS18B20_1_Sensor.py) and save the changes. In this example the script read the first ID called 25*, in the future, If you want to use several sensors, you will have to check IDs and add it into the new script.
<p>

- 5- Execute the script
<p> <em>sudo python DS18B20_1_Sensor.py</em>
<p>
---------------------------------------------------------------
<h2>Adding other DS18B20 Sensor</h2>

- 1- Connect the new sensor in parallel
- 2- Create a new Script using the code (DS18B20_2_Sensor.py or DS18B20_2_Sensor_V3.py). In this case we have two sensor ID, you can check your IDs in /sys/bus/w1/devices/ , set the right value IDs. Both Scripts show the temperature reading the file.  
- 3- Execute the script

<p>
---------------------------------------------------------------
<h2>Using DHT11 Sensor</h2>

The DHT11 Sensor measure temperature and humidity ,it is a small, cheap, digital sensor ideal to begin playing with sensors in the Raspberry Pi. There are different versions with 3 and 4 connectors (pins).

DHT11 (3 PINS)
- 1 - VCC connected to +3.3V~5V
- 2 - DATA connected to the microcontroller IO port
- 3 - GND connected to ground

DHT11 (4 PINS)
- 1 - VCC connected to +3.3V~5V
- 2 - DATA connected to the microcontroller IO port
- 3 - Null
- 4 - GND connected to ground

If you use this model, you have to connect a 4k7Ω-10kΩ resistor from the DATA pin to VCC.

- 1 - Connect the DHT11 to Raspberry Pi.

![alt tag](https://raw.github.com/rnieva/Playing-with-Sensors---Raspberry-Pi/master/scheme1_DHT11.png)

<p>VCC --> VCC
<p>Data --> GPIO 4 
<p>GND --> GND

- 2 - Create the script.
 After tried several ways to read data from the DTH11, I have chosen this. I’m using the Python library dht11.py provided by [szazo](https://github.com/szazo/DHT11_Python/blob/master/dht11.py). In fact you can find here a example perfect.
 Create a Script using the code (DTH11_Sensor.py).
- 3- Execute the script

------------------------------------------------------------------

<h2>PIR (IR motion Sensor)</h2>
This sensor allow you to sense motion, usually used to detect whether a human has moved in or out of the sensors range.
In this case, If the sensor detect any motion, a Led will blink.
<p>
- 1 - Connect the PIR and a LED to Raspberry Pi.
<p>

![alt tag](https://raw.github.com/rnieva/Playing-with-Sensors---Raspberry-Pi/master/scheme_PIR_LED.png)

- 2 - Create a new Script using the code (PIR_Sensor.py)
- 3 - Execute Script writing <em>sudo python PIR_Sensor.py</em>

-------------------------------------------------------------------




