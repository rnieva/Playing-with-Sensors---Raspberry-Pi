#!/usr/bin/env python
import MySQLdb
db = MySQLdb.connect("localhost", "root", "1234", "tempSensor1")
curs=db.cursor()

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'                       #location of connected devices
device_folder = glob.glob(base_dir + '28*')[0]          #'28*', If there is more tha one load the first
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

try:
    print(read_temp())
    temp_c, temp_f = read_temp()
    curs.execute ("""INSERT INTO dataSensor1
            values(CURRENT_DATE() - INTERVAL 1 DAY, NOW(), 'sensor1', %s)""",(temp_c))
    db.commit()
    print "Data committed"

except:
    print "Error: the database is being rolled back"
    db.rollback()
