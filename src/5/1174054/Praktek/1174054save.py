# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:36:50 2019

@author: Aulyardha Anindita
"""

import serial

def getDataLoop():
    ser = serial.Serial('COM5',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
getDataLoop()
