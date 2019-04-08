# -*- coding: utf-8 -*-
"""
Spyder Editor Izzah Hamka

This is a temporary script file.
"""
#no 2                
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)

import matplotlib.pyplot as plt
plt.plot([4,8,13,17,20],[54, 67, 98, 78, 45])
plt.xlabel('(Izza) Sumbu x') #Sumbu -X
plt.ylabel('(Izza) Sumbu y')#Sumbu -Y 
plt.show()

#no 4
#plt.legend()
#plt.xlabel('Days')
#plt.ylabel('Distance (kms)')

#no 5
import numpy as np
import matplotlib.pyplot as plt

x1 = np . linspace ( 1 , 2 )
x2 = np . linspace ( 1 , 5 )

plt . subplot(2,3,1)
plt . plot ( x1 , x2 , '2-' )
plt . title ( 'Subplot A' )
plt . subplot(2,3,2)
plt . plot ( x1 , x2 , 'o-' )
plt . title ( 'Subplot B' )
plt . subplot(2,3,3)
plt . title ( 'Subplot C' )
plt . subplot(2,3,4)
plt . title ( 'Subplot D' )
plt . subplot(2,3,5)
plt . title ( 'Subplot E' )
plt . subplot(2,3,6)
plt . title ( 'Subplot F' )

plt . show ()

#no 7
#population_age = [40,80,11,22,16,9,10,15,22,55,62,45,21,22,102,95,85,55,110,120,70,80,75,65,54,39,32,41,46,44]
#bins = [0,10,20,30,40,50,60,70,80,90,100]
#plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
#plt.xlabel('age groups')
#plt.ylabel('Number of people')
#plt.title('Histogram')
#plt.show()
#histogram
