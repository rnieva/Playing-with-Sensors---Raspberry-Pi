# Playing-with-Sensors---Raspberry-Pi
The goal of this repository is to show to user without any knowledge about sensors the easiest way to use them using a Raspberry Pi. Connect and Play. :)

------------------------------------------------------
<h2>Using a DS18B20 Temperature Sensor</h2>
Steps:

- 1- Download python and update if it's required
<p><em>sudo apt-get install python or python3</em>
<p><em>sudo apt-get update</em>
<p><em>sudo apt-get upgrade</em>
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

- 1 - Connect the PIR and a LED to Raspberry Pi.
<p>

![alt tag](https://raw.github.com/rnieva/Playing-with-Sensors---Raspberry-Pi/master/scheme_PIR_LED.png)

- 2 - Create a new Script using the code (PIR_Sensor.py)
- 3 - Execute Script writing <em>sudo python PIR_Sensor.py</em>

-------------------------------------------------------------------
<h2>Ultrasonic HC-SR04</h2>

A easy example  [here](https://github.com/rnieva/Ultrasonic-HC-SR04-Raspberry)

-------------------------------------------------------------------
<h2>DS18B20 Temperature Sensor in a Web Server</h2>

If you want see the temperature from a Web Browser, please you go on reading :) 
First of all we have to install a Web Server (Apache), a DB (MySQL) and a program language to store and retrive the data from the DB (PHPH).
0- Connect your DS18B20 sensor to Raspberry like the first example.

1- Execute next commands.
- sudo apt-get update and upgrade
- sudo apt-get install mysql-server python-mysqldb
- sudo apt-get install apache2 -y
- sudo apt-get install php5-mysql

2- Now you have to create a new Data Base using MySQL.
- mysql -u root -p
- CREATE DATABASE tempSensor1;
- CREATE TABLE dataSensor1 (tdate DATE, ttime TIME, sensor  TEXT, temperature FLOAT);
- quit

3- Create a script to read the temperature and store in DB.
- sudo nano dataDBRealSensor1.py, and copy the code from dataDBRealSensor1.py file you can find in this repository. 

4- Create a task in CRON (CRONTAB).
- sudo chmod +x dataDBRealSensor1.py --> to do a executable script
- crontab -e --> Choose any editor and add next line at the botton
- */1 * * * * /home/pi/./dataDBRealSensor1.py --> in this case the script will execute each 1 minute, you can setup the frecuency like you want, you only have to change the * by others parameters. [Info Cron](https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/) 
- crontab -r --> remove job

5- Create a file.php in our Apache server.
- cd /var/www/html/
- mv index.html index.php
- sudo nano index.php
- Copy the code from index.php that you can find in this repository

Now, from any web browser type the RaspberryPi IP Address, and you will able to the current temperature and all data previous store.

Also, you might download this [Project](https://github.com/rnieva/Web-Application-Show-Data-from-a-Raspberry-Pi) made in C# (.NET) and use it in a IIS (Internet Information Server) Web Server.
 
TIPS:
- Add a new user in MySQL to manage the DB.
- Change the MySQL config, sudo nano /etc/mysql/my.cnf, alter is bind-address --> 127.0.0.1 anse set up 0.0.0.0 to access from any host
- Setup a static IP. sudo nano /etc/network/interfaces --> Then change this line “iface eth0 inet dhcp” by “iface eth0 inet static“.
- Add any DNS Service

-------------------------------------------------------------------
