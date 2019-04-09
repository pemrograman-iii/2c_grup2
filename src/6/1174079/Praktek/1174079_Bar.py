# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:39:13 2019

@author: Chandra Kirana Poetra
"""

from matplotlib import pyplot as plt

def bar():

    hasil = 1174079 % 3 + 2
    
    for i in range(1, hasil):
        plt.subplot(2,2,i)
        plt.bar([2005,2006,2007,2008,2009,2010],[2000000000,2200000000,2300000000,2400000000,2500000000,2600000000],
        label="Indonesia",color='b',width=.3)
        plt.bar([2005,2006,2007,2008,2009,2010],[1000000000,1200000000,1300000000,1400000000,1500000000,1600000000],
        label="Malaysia",color='r',width=.3)
        plt.bar([2005,2006,2007,2008,2009,2010],[200000000,300000000,400000000,420000000,450000000,490000000],
        label="Singapore",color='g',width=.3)
        plt.legend()
        plt.xlabel('Tahun')
        plt.ylabel('Populasi')
        plt.title('Populasi Negara')
        plt.subplots_adjust(wspace=1, hspace=.7)
        
    plt.show()