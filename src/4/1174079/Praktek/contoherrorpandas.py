# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:23:54 2019

@author: Chandra Kirana Poetra
Politeknik Pos Indonesia
"""
import pandas

def nyobaintrycatch():
    try:
        da = pandas.read_csv("1174079.csv")
        print(da)
    except SyntaxError:
        print("Cek apabila ada typo")
    except NameError:
        print("Variable tidak ditemukan")
    except UnicodeDecodeError:
        print("ada yang salah di penulisan")
    except :
        ("terjadi kesalahan")

