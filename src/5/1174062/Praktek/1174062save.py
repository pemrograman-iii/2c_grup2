# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:46:33 2019

@author: Nurul Izza Hamka
"""

import serial

def getDataLoop():
    ser = serial.Serial('COM5',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
getDataLoop()