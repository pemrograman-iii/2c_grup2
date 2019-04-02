# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:22:27 2019

@author: Aulyardha Anindita
"""

#Teori Membuat Fungsi
import serial

def testArduino():
    ser = serial.Serial("COM5", 115200)
    print(ser.name)  

testArduino()