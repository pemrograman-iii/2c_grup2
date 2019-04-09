# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:07:43 2019

@author: Aulyardha Anindita
"""

from matplotlib import pyplot as plt

def tryExceptError():
    try:
        a=[1,2,3]
        y=[5,2,4]        
        plt.plot(x,y)        
        plt.show()        
    except SyntaxError:
        print("Perhatikan penulisan syntax!")
    except NameError:
        print("Variable yang anda cari tidak ada")
    except TypeError:
        print("Tipe data anda salah")
    except:
        print("Sepertinya ada sedikit masalah!")
        
tryExceptError()