# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:56:16 2019

@author: Difaal21
"""

# Jawaban 2
import serial

def getDataLoop():
    ser = serial.Serial('COM5',9600)
    while (1):
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
        
getDataLoop()