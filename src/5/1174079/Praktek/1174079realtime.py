# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:29:47 2019

@author: Chandra Kirana Poetra
"""

import serial

def ambildata():
    serX = serial.Serial('COM5',9600)
    print(serX.readline().decode("utf-8").strip('\n').strip('\r'))

ambildata()

import serial
import csv

def menuliscsv():
    serX = serial.Serial('COM5',9600)
    with open('praktex.csv', mode='w') as csv_file:
        fieldnames = ['contoh']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        while (1):
            data = serX.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'contoh': data})
            
menuliscsv()