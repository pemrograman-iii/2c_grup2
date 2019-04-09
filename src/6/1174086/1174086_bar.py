# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:32:45 2019

@author: acer
"""

# In[mod]:
print(1174086%3+2)

# In[No 1 Bar]:
from matplotlib import pyplot as plt

def bar():
    plt.subplot(231)
    plt.bar([.25,1.25,2.25,3.25,4.25], [40,50,60,70,80], 
    label="Jumlah", color='m',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75], [60,80,100,60,40], 
    label="Tahun", color='k', width=.5)
    plt.title('Contoh Bar 1')
    
    plt.subplot(232)
    plt.bar([.25,1.25,2.25,3.25,4.25], [30,70,60,100,80], 
    label="Jumlah", color='r',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75], [40,20,60,90,40], 
    label="Tahun", color='k', width=.5)
    plt.title('Contoh Bar 2')
    
    plt.subplot(233)
    plt.bar([.25,1.25,2.25,3.25,4.25], [10,30,60,80,40], 
    label="Jumlah", color='c',width=.5)
    plt.bar([.75,1.75,2.75,3.75,4.75], [30,45,70,60,70], 
    label="Tahun", color='k', width=.5)
    plt.title('Contoh Bar 3')
    plt.show()



