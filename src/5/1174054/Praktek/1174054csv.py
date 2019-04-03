# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:33:28 2019

@author: Aulyardha Anindita
"""

import csv

def readCsv():
    with open('praktek.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jarak'])
            
readCsv()