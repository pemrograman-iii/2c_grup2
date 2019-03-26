# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:29:57 2019

@author: D. Irga B. Naufal Fakhri
"""

import lib_1174066_pandas

# Membuat file baru
lib_1174066_pandas.writepanda('1174066.csv','1174066_baru_pandas.csv')

# Membaca file csv panda
# Dataframe
lib_1174066_pandas.readpanda('1174066.csv')
# Dictionary
lib_1174066_pandas.readpandadict('1174066.csv')