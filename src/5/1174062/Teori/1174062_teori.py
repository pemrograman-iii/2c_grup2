# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:28:21 2019

@author: Nurul Izza Hamka
"""

import serial

def testArduino():
    ser = serial.Serial("COM5", 115200)
    print(ser.name)  

testArduino()