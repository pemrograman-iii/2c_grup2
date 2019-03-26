# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:51:33 2019

@author: Chandra Kirana Poetra
Politeknik pos indonesia
"""

import pandas

def exampleofhowtoreadpanda(a):
    df = pandas.read_csv(a)
    print(df)
    
def exampleofreadpandausingdict(a):
    df = pandas.read_csv(a).to_dict()
    print(df)
    
def exampleofreadchangedateformatpandas(a):
    df = pandas.read_csv(a, index_col='npm', parse_dates=['tanggallahir'])
    print(df)
    
def exampleofhowtochangeindexinpandas(a):
    df = pandas.read_csv(a, index_col='npm')
    print(df)

def exampleofhowtorenameacolumm(a):
    df = pandas.read_csv(a, header=0, names=['Student ID', 'Full Name','Class', 'Date of birth'])
    print(df)
    
def examplehowtowritepanda(a,b):
    df = pandas.read_csv(a, 
            index_col='npm', 
            parse_dates=['tanggallahir'],
            header=0, 
            names=['No', 'Nama', 'NPM', 'tanggallahir'])
    df.to_csv(b)