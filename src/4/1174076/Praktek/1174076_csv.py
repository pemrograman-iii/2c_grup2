# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:22:29 2019

@author: Difaal21
"""

import csv

#Jawaban Nomor 1
def Satu():
    f = open('coba.csv', 'r')
    reader = csv.reader(f)
    
    for row in reader:
        print (row)
Satu()
print('')

            
#Jawaban Nomor 2
def Dua():
    with open('coba.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
Dua()
print('')
 
# Jawaban Nomor 8
def Delapan():
    with open('buatfile.csv', mode='w') as csv_file:
            fieldnames = ['Npm', 'Nama', 'Kelas', 'Tanggal lahir']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
            writer.writeheader()
            writer.writerow({'Npm': '1174076', 'Nama': 'Difa Al Fansha', 'Kelas': 'D4 TI 2C', 'Tanggal lahir': '02-05-1999'})
            writer.writerow({'Npm': '6704711', 'Nama': 'Fansha Al Difa', 'Kelas': 'D4 TI 2C', 'Tanggal lahir': '06-06-1999'})
Delapan()
        