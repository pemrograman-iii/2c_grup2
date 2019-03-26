# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:03:09 2019

@author: D. Irga B. Naufal Fakhri
"""

import lib_1174066_csv

# Membuat file csv baru yang isinya npm, nama, kelas dan tanggallahir
lib_1174066_csv.write('1174066_csv_baru.csv')

# Membaca file csv
# List
lib_1174066_csv.read('1174066.csv')
# Dictionary
lib_1174066_csv.readdict('1174066.csv')