# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:15:06 2019

@author: Izza Hamka
"""

from matplotlib import pyplot as plt

def pie():

    hasil = 1174062 % 3 + 2
    
    potong = [8,6,5,4]
    kegiatan = ['Kulineran','Shopping','Menonton','Jogging']
    kolom = ['m','r','g','c']
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.pie(potong,
        labels=kegiatan,
        colors=kolom,
        startangle=90,
        shadow= True,
        explode=(0,0,0.2,0),
        autopct='%1.1f%%')         
        plt.title('Schedulle Mingguan')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()