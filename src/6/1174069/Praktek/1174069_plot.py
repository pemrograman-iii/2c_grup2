# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:13:39 2019

@author: FannyCantik
"""

from matplotlib import pyplot as plt

def plot():

    hasil = 1174069 % 3 + 2
    
    x = [2014,2015,2016,2017,2018,2019]
    y = [76,87,105,122,148,170]
    x2 = [2014,2015,2016,2017,2018,2019]
    y2 = [78,97,114,134,146,167]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        x = [2014,2015,2016,2017,2018,2019]
        y = [50,99,120,150,270,300]
        x2 = [2014,2015,2016,2017,2018,2019]
        y2 = [55,150,160,200,250,295]
        plt.plot(x,y,'g',label='Army (BTS FANS)', linewidth=1)
        plt.plot(x2,y2,'y',label='EXO-L (EXO FANS)',linewidth=1)
        plt.title('BTS VS EXO')
        plt.ylabel('Jumlah Penggemar')
        plt.xlabel('Tahun')
        plt.legend()
        plt.grid(True,color='k')

        plt.subplots_adjust(wspace=.4, hspace=.7)
    
    plt.show()
    
