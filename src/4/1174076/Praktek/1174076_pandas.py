# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:51:10 2019

@author: Difaal21
"""


import pandas

# Jawaban Nomor 3
def Tiga():
    a = pandas.read_csv('coba.csv')
    print(a)
Tiga()
print('')

# Jawaban Nomor 4
def Empat():
    a = pandas.read_csv('coba.csv')
    b = pandas.DataFrame.from_dict(a)
    print(b)
Empat()
print ('')

# jawaban Nomor 5
def Lima():
    a = pandas.read_csv('coba.csv', parse_dates=['Tanggal lahir'])
    print(a)
Lima()
print ('')

# Jawaban Nomor 6
def Enam():
    a = pandas.read_csv('coba.csv')
    a.index = ['Informasi', 'Informasi 2']
    print(a)
Enam()
print ('')

# Jawaban Nomor 7
def Tujuh():
    a = pandas.read_csv('coba.csv')
    a.columns =['NPM mu', 'Nama bro', 'Kelas gan', 'Tanggal lahir coy'] 
    print(a)
Tujuh()
print ('')

# Jawaban Nomor 9
def Sembilan():
    a = pandas.read_csv('coba.csv', 
                index_col='NPM', 
                parse_dates=['Tanggal Lahir'],
                header=0, 
                names=['NPM', 'Nama', 'Kelas', 'Tanggal Lahir'])
    a.to_csv('nyoba.csv')
print(Sembilan)

