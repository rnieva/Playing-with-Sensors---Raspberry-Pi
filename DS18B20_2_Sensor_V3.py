import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#Sensor IDs
id1 = '28-031646f191ff'
id2 = '28-03167526c6ff'
base_dir = '/sys/bus/w1/devices/' #location of connected devices

def read_temp_raw(id):
    device_folder = glob.glob(base_dir + id)[0]
    device_file = device_folder + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(id):
    lines = read_temp_raw(id)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.3)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

while True:
        print ('Sensor1= ', read_temp(id1))
        time.sleep(1)
        print ('Sensor2= ', read_temp(id2))
	time.sleep(1)
