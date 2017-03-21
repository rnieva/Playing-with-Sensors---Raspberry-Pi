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
<p>Sensor DS18B20 with cable
<p>Black --> GND
<p>Yellow --> GPIO 4 
<p>Red --> VCC 3.3v
<p>
<p>Sensor DS18B20 without cable
<p>From plane face:
<p>Left leg --> GND
<p>Center leg --> GPIO 4 
<p>Right leg --> VCC 3.3v
<p>


- 3- Edit config.txt
<p>sudo nano /boot/config.txt
<p>Add dtoverlay=w1-gpio on the bottom of the file 
<p>sudo reboot
<p>


- 4- 
<p>ls -l /sys/bus/w1/devices/ --> It show a list of the devices currently connected to your Raspberry Pi
<p>sudo nano test_sensor1.py --> Create a new python file
<p>Copy the code (DS18B20_1_Sensor.py) and save the changes
<p>


- 5- Execute script
<p>sudo python DS18B20_1_Sensor.py
<p>
---------------------------------------------------------------
