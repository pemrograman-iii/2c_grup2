# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:05:44 2019

@author: Aulyardha Anindita
"""

from matplotlib import pyplot as plt

def pie():

    hasil = 1174054 % 3 + 2
    
    potong = [8,6,5,4]
    kegiatan = ['Tidur','Kuliah','Main','Belajar']
    kolom = ['c','m','g','w']
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.pie(potong,
        labels=kegiatan,
        colors=kolom,
        startangle=90,
        shadow= True,
        explode=(0,0,0.2,0),
        autopct='%1.1f%%')         
        plt.title('Aktivitas Sehari-hari Dita')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()