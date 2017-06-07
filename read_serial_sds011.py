#!/usr/bin/python
import time
import serial
import urllib.request
user = 118
s = 1
loop = 0

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.9)

pm25 = 0
pm10 = 0
while True:
    d = ser.readline()
    if d[0] == 0xaa and d[1] == 0xc0 and d[9] == 0xab:
        pm25 = d[2] + d[3] *256;
        pm10 = d[4] + d[5] *256;
    else:
        print("skip seq: ", d[0], d[1], d[8])
    loop += 1
    if loop > 60:
        param = "&format=2&serial="+ str(s) +"&items=0-D-"+ str(pm25) +",1-D-"+ str(pm10)
        print(param)
        f = urllib.request.urlopen('http://61.74.178.129:8080/logone?user=' + str(user) + param)
        print(str(f.read()))
        loop = 0
        s += 1
    else:
        print(pm25, pm10)
