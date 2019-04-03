# -*- coding: utf-8 -*-
"""
Chapter 5 Praktek

author: D. Irga B. Naufal Fakhri.
"""
import serial

def ReadSerialLoop():
    ser = serial.Serial("COM3",9600)
    while (1):
        read = ser.readline().decode("utf-8").strip('\n').strip('\r')
        print(read)
    
ReadSerialLoop()