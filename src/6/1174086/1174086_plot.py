# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:41:04 2019

@author: acer
"""

# In[No Plot]
import matplotlib.pyplot as plt

def plot():    
    x = [5,3,5]
    y = [5,8,10]
    plt.subplot(231)
    plt.plot(x,y)
    plt.ylabel('Sumbu Y')
    plt.xlabel('Sumbu X')
    
    x1 = [6,3,5]
    y1 = [4,8,10]
    plt.subplot(232)
    plt.plot(x1,y1)
    plt.ylabel('Sumbu Y')
    plt.xlabel('Sumbu X')
    
    x2 = [5,7,9]
    y2= [6,4,7]
    plt.subplot(233)
    plt.plot(x2,y2)
    plt.ylabel('Sumbu Y')
    plt.xlabel('Sumbu X')
    plt.show()
plot()