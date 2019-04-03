# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:39:59 2019

@author: Chandra Kirana Poetra
"""

import serial

def ambildata():
    serX = serial.Serial('COM5',9600)
    while (1):
        print(serX.readline().decode("utf-8").strip('\n').strip('\r'))
        
ambildata()