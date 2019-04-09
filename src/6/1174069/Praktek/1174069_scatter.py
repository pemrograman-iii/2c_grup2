# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:17:43 2019

@author: FannyCantik
"""

from matplotlib import pyplot as plt

def scatter():

    hasil = 1174006 % 3 + 2
    
    x = [1,2,3,4.5,5,6,6.5]
    y = [7.5,8,9,9.5,10,11,11.5]
 
    x1=[2,3.5,4,5.5,6,7.5,10]
    y1=[3,3.5,4,5,6,7,8.5]
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.scatter(x,y, label='Pengguna Android',color='g')
        plt.scatter(x1,y1,label='Pengguna IPhone',color='k')
        plt.xlabel('Android')
        plt.ylabel('IPhone')
        plt.title('Scatter Plot')
        plt.legend()
        plt.subplots_adjust(wspace=1.1, hspace=.7)
    
    plt.show()
    