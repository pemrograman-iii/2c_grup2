# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:06:04 2019

@author: Fanny_Cantik
"""

from matplotlib import pyplot as plt

def bar():

    hasil = 1174069 % 3 + 2
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.bar([2012.7,2013.7,2014.7,2015.7,2016.7,2017.7],[8000,8500,10000,20000,30000,35000],
        label="Instagram",color='c',width=.3)
        plt.bar([2013,2014,2015,2016,2017,2018],[10000,15000,30000,35000,40000,45000],
        label="Facebook",color='y',width=.3)
        plt.bar([2013.3,2014.3,2015.3,2016.3,2017.3,2018.3],[7000,6500,7000,8500,9000,10000],
        label="Twitter",color='g',width=.3)
        plt.legend()
        plt.xlabel('Tahun')
        plt.ylabel('Jumlah Pengguna')
        plt.title('Pengguna Sosial Media Dari Tahun ke Tahun')
        plt.subplots_adjust(wspace=1, hspace=.7)
        
       
   
    plt.show()

    