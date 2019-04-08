"""
Tugas Chapter 6 Teori

@author: D. Irga B. Naufal Fakhri
"""
#%% Plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [13, 17, 19, 33]
plt.plot(x, y)
plt.show()

#%% Bar
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [13, 17, 19, 33]
plt.bar(x, y)
plt.show()

#%% Histogram
import matplotlib.pyplot as plt
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
plt.hist(x, 5)
plt.show()

#%% Histogram
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100)
y = np.random.randn(100)
x1 = np.random.randn(100)
y1 = np.random.randn(100)
plt.scatter(x,y, label='Angka Random 1',color='R')
plt.scatter(x1,y1, label='Angka Random 2',color='B')
plt.xlabel('Random 1')
plt.ylabel('Random 2')
plt.title('Diagram Titik')
plt.legend()
plt.show()
#%% Stack Plot
hari = [1,2,3,4,5,6,7]
tidur =[7,8,6,8,7,9,10]
makan = [2,3,4,3,2,3,4]
kerja =[7,8,7,2,2,6,0]
main = [8,5,7,8,13,15,25]
  
plt.plot([],[],color='m', label='Tidur', linewidth=5)
plt.plot([],[],color='c', label='Makan', linewidth=5)
plt.plot([],[],color='r', label='Kerja', linewidth=5)
plt.plot([],[],color='k', label='Main', linewidth=5)
 
plt.stackplot(hari, tidur,makan,kerja,main, colors=['b','m','r','c'])
  
plt.xlabel('Hari')
plt.ylabel('Lamanya')
plt.title('Stack Plot')
plt.legend()
plt.show()
#%% Subplot
x = [1,2,3,4,5]
y = [6,7,8,9,10]
plt.subplot(331)#tinggi,lebar,urutan
plt.plot(x, y)
plt.subplot(332)
plt.bar(x, y)
plt.subplot(333)
plt.hist(x, 2)
plt.subplot(334)
plt.scatter(x, y)
plt.subplot(335)#tinggi,lebar,urutan
plt.plot(x, y)
plt.subplot(336)
plt.bar(x, y)
plt.subplot(337)
plt.hist(x, 2)
plt.subplot(338)
plt.scatter(x, y)
plt.subplot(339)
plt.hist(x, 2)
plt.show()
#%% Histogram 2
import matplotlib.pyplot as plt
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
plt.hist(x, 5,  histtype ='bar' , rwidth =0.8)
plt.xlabel('Angka')
plt.ylabel('Banyaknya angka rentang dari 5')
plt.show()
