# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:38:47 2019

@author: FannyCantik
"""

import csv

#No. 1
def bukaModeListCsv():
    with open('teori.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#No. 2            
def bukaModeDictCsv():
    with open('teori.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('teori6.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1174999', 'nama': 'Fanny', 'kelas': 'D4TI2C', 'tanggal lahir': '17/09/1999'})
        writer.writerow({'npm': '1174888', 'nama': 'Shafira', 'kelas': 'D4TI2C', 'tanggal lahir': '19/09/1999'})
