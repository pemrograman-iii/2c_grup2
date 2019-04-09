# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:37:49 2019

@author: Chandra Kirana Poetra
"""

from matplotlib import pyplot as plt

def tryExceptError():
    try:
        a=[1,2,3]
        b=[5,2,4]        
        plt.plot(x,y)        
        plt.show()        
    except SyntaxError:
        print("Kesalahan pada penulisan syntax")
    except NameError:
        print("Variable yang anda maksud tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi error")
        
tryExceptError()