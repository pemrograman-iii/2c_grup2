# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:06:21 2019

@author: Aulyardha Anindita
"""

from matplotlib import pyplot as plt

def plot():

    hasil = 1174054 % 3 + 2
    
    x = [2014,2015,2016,2017,2018,2019]
    y = [80,120,95,110,130,150]
    x2 = [2014,2015,2016,2017,2018,2019]
    y2 = [90,100,120,140,160,180]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.plot(x,y,'r',label='Descendants Of The Sun', linewidth=1)
        plt.plot(x2,y2,'k',label='Touch My Heart',linewidth=1)
        plt.title('Drama Korea Dita')
        plt.ylabel('Rating')
        plt.xlabel('Tahun')
        plt.legend()
        plt.grid(True,color='c')
        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()