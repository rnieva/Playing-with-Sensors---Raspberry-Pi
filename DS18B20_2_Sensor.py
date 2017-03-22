#!/usr/bin/python
import time

def gettemp(id): #Open the file to read the info
  try:
    mytemp = ''
    f = open('/sys/bus/w1/devices/' + id + '/w1_slave', 'r')
    line = f.readline()
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline()
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()

    return int(mytemp[1])

  except:
    return 99999

if __name__ == '__main__':
  # Add sensors IDs
  id = '28-03167526c6ff'
  id2= '28-031646f191ff'
  while True:
        print "Sensor1 Temp : " + '{:.3f}'.format(gettemp(id)/float(1000))
        print "Sensor2 Temp : " + '{:.3f}'.format(gettemp(id2)/float(1000))
        time.sleep(1)
