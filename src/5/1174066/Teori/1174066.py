# -*- coding: utf-8 -*-
"""
Chapter 5 Teori

author: D. Irga B. Naufal Fakhri.
"""
import serial

def ReadSerial():
    ser = serial.Serial("COM3",9600)
    read = ser.readline()
    print(read)

ReadSerial()