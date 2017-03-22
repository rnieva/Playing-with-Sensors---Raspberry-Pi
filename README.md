# Playing-with-Sensors---Raspberry-Pi
DS18B20 Temperature Sensor
<p>
<h2>Using only a DS18B20 Temperature Sensor</h2>
<p>
Steps:
<p>


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
<p>Copy the code (DS18B20_1_Sensor.py) and save the changes. In this example the script read the first ID called 25*, in the future, If you can use several sensors, you will have to check IDs and write it into the script.
<p>

- 5- Execute the script
<p>sudo python DS18B20_1_Sensor.py
<p>
---------------------------------------------------------------
<h2>Adding other DS18B20 Sensor</h2>

- 1- Connect the new sensor in parallel
- 2- Create a new Script using the code ((DS18B20_2_Sensor.py) or (DS18B20_2_Sensor_V3.py)). In this case we have two sensor ID, you can check IDs in /sys/bus/w1/devices/. Both Scripts show the temperature reading the file.  
- 3- Execute the script

<p>
---------------------------------------------------------------
<h2>Using DHT11 Sensor</h2>

