# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:59:40 2019

@author: Difaal21
"""


# Jawaban 4
import csv

def readCsv():
    with open('ujicoba.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['angka'])
            
readCsv()