# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:39:20 2019

@author: FannyCantik
"""
import csv

def readCsv():
    with open('praktek.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jarak'])
            
readCsv()
