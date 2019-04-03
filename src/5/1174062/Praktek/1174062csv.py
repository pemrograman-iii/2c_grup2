# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:44:18 2019

@author: Nurul Izza Hamka
"""

import csv

def readCsv():
    with open('praktek.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['jarak'])
            
readCsv()