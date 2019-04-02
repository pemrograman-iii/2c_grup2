# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:20:23 2019

@author: Chandra Kirana Poetra
"""
import serial

def bacaserialarduino():
    variableserial = serial.Serial("COM1",9600)
    baca = variableserial.readline()
    print(baca)

bacaserialarduino()
