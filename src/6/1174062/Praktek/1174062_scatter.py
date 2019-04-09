# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:20:57 2019

@author: Nurul Izza Hamka
"""


from matplotlib import pyplot as plt

def scatter():

    hasil = 1174062 % 3 + 2
    
    x = [2,1.3,2,4.5,3,3.5,6.6]
    y = [7.5,8,8.5,9,9.5,10,10.5]
     
    x1=[8,8.5,9,9.5,10,10.5,11]
    y1=[3,3.5,3.7,4,4.5,5,5.2]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.scatter(x,y, label='Untung',color='m')
        plt.scatter(x1,y1,label='Rugi',color='c')
        plt.xlabel('Pendapatam Per Tahun')
        plt.ylabel('Rugi Per Bulan')
        plt.title('Scatter Plot Nurul')
        plt.legend()
        plt.subplots_adjust(wspace=1.1, hspace=.7)
    
    plt.show()