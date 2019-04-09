# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:39:51 2019

@author: Chandra Kirana Poetra
"""

from matplotlib import pyplot as plt

def pie():

    hasil = 1174079 % 3 + 2
    
    potong = [7,4,2,12]
    activity = ['Game','MeTime','Kuliah','Bebas']
    kolom = ['c','m','y','g']
    
    for i in range(1, hasil):
        plt.subplot(2,2,i)
        plt.pie(potong,
        labels=activity,
        colors=kolom,
        startangle=90,
        explode=(0,0,0.2,0),
        autopct='%1.1f%%')         
        plt.title('Aktivitas Sehari hari')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()