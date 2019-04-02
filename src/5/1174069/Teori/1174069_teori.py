# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:21:03 2019

@author: FannyCantik
"""
import serial

def testArduino():
    ser = serial.Serial("COM5", 115200)
    print(ser.name)  

testArduino()
