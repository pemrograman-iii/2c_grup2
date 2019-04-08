# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:34:09 2019

@author: Chandra Kirana Poetra
"""
#%% Plot Chart
import matplotlib.pyplot as librarymatplotlib
x = [1, 2, 3, 4, 5]
y = [10, 12, 30, 46, 55]
librarymatplotlib.plot(x, y)
librarymatplotlib.show()

#%% Bar Chart
import matplotlib.pyplot as librarymatplotlib
x = [1, 2, 3, 4, 5]
y = [10, 12, 30, 46, 55]
librarymatplotlib.bar(x, y)
librarymatplotlib.show()
#%% Histogram chart
import matplotlib.pyplot as librarymatplotlib
x = [10,20,30,25,22,55,11,33,22,55,88,44,100]
librarymatplotlib.hist(x, 5)
librarymatplotlib.show()
#%% Diagram Histogram
import matplotlib.pyplot as librarymatplotlib
import numpy as npy
x = npy.random.randn(100)
y = npy.random.randn(100)
x1 = npy.random.randn(100)
y1 = npy.random.randn(100)
librarymatplotlib.scatter(x,y, label='Contoh 1',color='m')
librarymatplotlib.scatter(x1,y1, label='Contoh 2',color='B')
librarymatplotlib.xlabel('Contoh 1')
librarymatplotlib.ylabel('Contoh 2')
librarymatplotlib.title('Diagram Swarm')
librarymatplotlib.legend()
librarymatplotlib.show()
#%% Stack Plot diagram
hari = [1,2,3,4,5,6,7]
Gaming =[9,5,3,5,7,3,2]
Belajar = [1,2,3,4,5,6,7]
kerja =[1,2,3,4,3,4,6]
Freetime = [8,5,7,8,13,15,25]
  
librarymatplotlib.plot([],[],color='m', label='Gaming', linewidth=5)
librarymatplotlib.plot([],[],color='c', label='Belajar', linewidth=5)
librarymatplotlib.plot([],[],color='r', label='Kerja', linewidth=5)
librarymatplotlib.plot([],[],color='k', label='Freetime', linewidth=5)
 
librarymatplotlib.stackplot(hari, Gaming,Belajar,kerja,Freetime, colors=['b','m','c','r','k'])
  
librarymatplotlib.xlabel('Hari')
librarymatplotlib.ylabel('Durasi')
librarymatplotlib.title('Stack Plot Diagram')
librarymatplotlib.legend()
librarymatplotlib.show()

#%% Subplot diagram
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,5,2,3,7,9,10,4,5,7]
librarymatplotlib.subplot(331)
librarymatplotlib.plot(x, y)
librarymatplotlib.subplot(332)
librarymatplotlib.bar(x, y)
librarymatplotlib.subplot(333)
librarymatplotlib.hist(x, 2)
librarymatplotlib.subplot(334)
librarymatplotlib.scatter(x, y)
librarymatplotlib.subplot(335)
librarymatplotlib.plot(x, y)
librarymatplotlib.subplot(336)
librarymatplotlib.bar(x, y)
librarymatplotlib.subplot(337)
librarymatplotlib.hist(x, 2)
librarymatplotlib.subplot(338)
librarymatplotlib.scatter(x, y)
librarymatplotlib.subplot(339)
librarymatplotlib.hist(x, 2)
librarymatplotlib.show()
#%% Histogram diagram
import matplotlib.pyplot as librarymatplotlib
x = [10,20,30,15,23,12,66,44,33,22,33,11,23,55,11,22,77,99,22]
librarymatplotlib.hist(x, 5,  histtype ='bar' , rwidth =0.8)
librarymatplotlib.xlabel('Angka')
librarymatplotlib.ylabel('Rentang dari 5')
librarymatplotlib.show()