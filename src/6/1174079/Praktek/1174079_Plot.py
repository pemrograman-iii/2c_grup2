# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:40:34 2019

@author: Chandra Kirana Poetra
"""

from matplotlib import pyplot as plt

def plot():

    hasil = 1174079 % 3 + 2
    
    x = [2001,2002,2003,2004,2005,2006]
    y = [10,20,50,70,90,110]
    x2 = [2001,2002,2003,2004,2005,2006]
    y2 = [30,20,30,50,90,130]
    
    for i in range(1, hasil):
        plt.subplot(2,2,i)
        plt.plot(x,y,'b',label='Sample A', linewidth=1)
        plt.plot(x2,y2,'r',label='Sample B',linewidth=1)
        plt.title('Sample')
        plt.ylabel('Jumlah Mikroba')
        plt.xlabel('Tahun')
        plt.legend()
        plt.grid(True,color='k')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()
    