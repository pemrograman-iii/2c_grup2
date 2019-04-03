# -*- coding: utf-8 -*-
"""
Chapter 5 Praktek

author: D. Irga B. Naufal Fakhri.
"""
import csv
   
def read(namafile):
    with open(namafile, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['Ready'])
            
read("1174066.csv")