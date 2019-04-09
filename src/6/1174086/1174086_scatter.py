# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:38:55 2019

@author: acer
"""

# In[Scatter]:
import matplotlib.pyplot as plt

def scatter():
    x = [1,1.5,2,2.5,3,3.5,3.7]
    y = [7.5,8,8.5,9,9.5,10,10.5]
    
    s = [8,8.5,9,9.5,10,10.5,11]
    a = [3,3.5,3.7,4,4.5,5,5.2]
    plt.subplot(231)
    plt.scatter(x,y, label='high income', color='k')
    plt.scatter(s,a, label='low income', color='b')
    plt.title('Scatter Pertama')
    
    
    plt.subplot(232)
    plt.scatter(x,y, label='high income', color='r')
    plt.scatter(s,a, label='low income', color='m')
    plt.title('Scatter kedua')
    
    
    plt.subplot(233)
    plt.scatter(x,y, label='high income', color='b')
    plt.scatter(s,a, label='low income', color='y')
    plt.title('Scatter ketiga')
    plt.show()

