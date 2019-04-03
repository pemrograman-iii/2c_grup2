# -*- coding: utf-8 -*-
"""
Chapter 5 Praktek

author: D. Irga B. Naufal Fakhri.
"""
import serial

def ReadSerial():
    ser = serial.Serial("COM3",9600)
    read = ser.readline().decode("utf-8").strip('\n').strip('\r')
    print(read)

ReadSerial()

import csv
def write():
    with open("1174066.csv", mode='w') as nama_file:
        tulis_file = csv.writer(nama_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ser = serial.Serial("COM3",9600)
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        tulis_file.writerow([read])
        
write()