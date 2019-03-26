# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:51:33 2019

@author: Chandra Kirana Poetra
Politeknik pos indonesia
"""
import csv

def readcsvfile(namafile):
    with open(namafile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\tNomor No: {row[0]} Nama: {row[1]} NPM: {row[2]}.')
                line_count += 1
                print(f'Processed {line_count} lines.')
                
def readdengandict(a):
    with open(a, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\tNomor No: {row["No"]} Nama: {row["Nama"]} NPM: {row["NPM"]} ')
            line_count += 1
        print(f'Processed {line_count} lines.')

def write(a):
    with open(a, mode='w') as exampleofhowtowrite:
        tulis_file = csv.writer(exampleofhowtowrite, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        tulis_file.writerow(['No', 'Nama', 'NPM', 'tanggallahir'])
        tulis_file.writerow(['1', 'Chandra Kirana Poetra', '1174079', '05/09/99'])