# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:22:52 2019

@author: Nurul Izza 
"""

from matplotlib import pyplot as plt

def plot():

    hasil = 1174062 % 3 + 2
    
    x = [2014,2015,2016,2017,2018,2019]
    y = [20,50,100,150,160,170]
    x2 = [2014,2015,2016,2017,2018,2019]
    y2 = [10,20,100,160,165,170]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.plot(x,y,'r',label='Novel', linewidth=1)
        plt.plot(x2,y2,'k',label='Ensiklopedia',linewidth=1)
        plt.title('Penilaian Pembaca')
        plt.ylabel('Rating')
        plt.xlabel('Tahun')
        plt.legend()
        plt.grid(True,color='c')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()