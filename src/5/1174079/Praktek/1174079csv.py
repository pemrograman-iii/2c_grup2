# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:41:01 2019

@author: Chandra Kirana Poetra
"""

import csv

def bacafilecsv():
    with open('praktex.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['contoh'])
            
bacafilecsv()