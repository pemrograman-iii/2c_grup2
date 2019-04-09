# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:40:09 2019

@author: acer
"""

# In[Pie Chart]:
import matplotlib.pyplot as plt

def pie():
    slices = [7,2,2,13]
    aktifitas = ['dokter','polisi','guru','pilot']
    cols = ['r', 'y', 'b', 'c']
    plt.subplot(231)
    plt.pie(slices,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0,0.1,0),
            autopct='%1.1f%%')
    
    plt.title('Contoh Pie')
    aktifitas = ['nanas','mangga','melon','jambu']
    cols = ['y', 'g', 'b', 'm']
    plt.subplot(232)
    plt.pie(slices,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0,0.1,0),
            autopct='%1.1f%%')
    
    aktifitas = ['merah','kuning','hijau','biru']
    cols = ['r', 'y', 'g', 'b']
    plt.title('Contoh Pie')
    plt.subplot(233)
    plt.pie(slices,
            labels=aktifitas,
            colors=cols,
            startangle=90,
            shadow= True,
            explode=(0,0,0.1,0),
            autopct='%1.1f%%')
    plt.title('Contoh Pie')
    plt.show()




