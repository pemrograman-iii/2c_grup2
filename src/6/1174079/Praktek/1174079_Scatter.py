# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:41:17 2019

@author: Chandra Kirana Poetra
"""

from matplotlib import pyplot as plt

def scatter():

    hasil = 1174079 % 3 + 2
    
    x = [1,2,5,2,6,8,2,4,7,10]
    y = [5,5,5,7,1,3,6,8,6,5]
     
    x1=[5,5,5,7,1,3,6,8,6,5]
    y1=[1,2,5,2,6,8,2,4,7,10]
    
    for i in range(1, hasil):
        plt.subplot(2,2,i)
        plt.scatter(x,y, label='pendapatan tinggi simpanan rendah',color='r')
        plt.scatter(x1,y1,label='pendapatan rendah simpanan tinggi',color='g')
        plt.xlabel('simpanan dalam ratusan')
        plt.ylabel('pendapatan dalam ribuan')
        plt.title('Scatter Plot')
        plt.legend()
        plt.subplots_adjust(wspace=1.1, hspace=.7)
    
    plt.show()