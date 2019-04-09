# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:09:30 2019

@author: FannyCantik
"""

from matplotlib import pyplot as plt

def pie():

    hasil = 1174069 % 3 + 2
    
    potong = [10,2,7,5]
    kegiatan = ['Tidur','Makan','Nonton Drakor','Main']
    kolom = ['r','b','y','g']
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.pie(potong,
        labels=kegiatan,
        colors=kolom,
        startangle=90,
        shadow= True,
        explode=(0,0,0.2,0),
        autopct='%1.1f%%')
 
        plt.title('Hari Liburku')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()
    