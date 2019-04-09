# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:36:59 2019

@author: FannyCantik
"""
# In[1]: Jawaban No. 2
from matplotlib import pyplot as plt
 
x=[1,2,3]
y=[5,2,4]

plt.plot(x,y)

plt.show()

# In[2]: Bar Graph

from matplotlib import pyplot as plt

plt.bar([2012.7,2013.7,2014.7,2015.7,2016.7,2017.7],[8000,8500,10000,20000,30000,35000],
label="Instagram",color='c',width=.3)
plt.bar([2013,2014,2015,2016,2017,2018],[10000,15000,30000,35000,40000,45000],
label="Facebook",color='y',width=.3)
plt.bar([2013.3,2014.3,2015.3,2016.3,2017.3,2018.3],[7000,6500,7000,8500,9000,10000],
label="Twitter",color='g',width=.3)
plt.legend()
plt.xlabel('Tahun')
plt.ylabel('Jumlah Pengguna')
plt.title('Pengguna Sosial Media Dari Tahun ke Tahun')
plt.show()

# In[3]: Histogram

import matplotlib.pyplot as plt
orang = [11,22,16,9,10,15,22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48,50,29,14,68]
umur = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(orang, umur, histtype='bar', rwidth=0.8)
plt.xlabel('Umur')
plt.ylabel('Jumlah Orang')
plt.title('Histogram')
plt.show()

# In[4]: Scatter Plot

import matplotlib.pyplot as plt
x = [1,2,3,4.5,5,6,6.5]
y = [7.5,8,9,9.5,10,11,11.5]
 
x1=[2,3.5,4,5.5,6,7.5,10]
y1=[3,3.5,4,5,6,7,8.5]
 
plt.scatter(x,y, label='Pengguna Android',color='g')
plt.scatter(x1,y1,label='Pengguna IPhone',color='k')
plt.xlabel('Android')
plt.ylabel('IPhone')
plt.title('Scatter Plot')
plt.legend()
plt.show()

# In[5]: Area plot

import matplotlib.pyplot as plt
libur = [1,2,3,4,5]
  
tidur =[7,8,6,11,7]
makan = [2,3,4,3,4]
nonton_drakor =[7,8,7,2,5]
main = [8,5,7,8,13]
  
plt.plot([],[],color='r', label='Tidur', linewidth=5)
plt.plot([],[],color='b', label='Makan', linewidth=5)
plt.plot([],[],color='y', label='Nonton Drakor', linewidth=5)
plt.plot([],[],color='g', label='Main', linewidth=5)
  
plt.stackplot(libur,tidur,makan,nonton_drakor,main, colors=['r','b','y','g'])
  
plt.xlabel('x')
plt.ylabel('y')
plt.title('Hari Liburku')
plt.legend()
plt.show()

# In[6]: Pie Plot
import matplotlib.pyplot as plt

potong = [10,2,7,5]
kegiatan = ['Tidur','Makan','Nonton Drakor','Main']
kolom = ['r','b','y','g']
 
plt.pie(potong,
  labels=kegiatan,
  colors=kolom,
  startangle=90,
  shadow= True,
  explode=(0,0,0.2,0),
  autopct='%1.1f%%')
 
plt.title('Hari Liburku')
plt.show()

# In[7]: Line

from matplotlib import pyplot as plt
 
y = [1000,5000,12000,13000,14500,18000]
x = [2014,2015,2016,2017,2018,2019]
plt.plot(x,y)
plt.title('Pemakai Anastasia Beberly Hills')
plt.ylabel('Jumlah Pemakai Jumlah Anastasia Beverly Hills')
plt.xlabel('Tahun')
plt.show()

# In[8]: Jawaban No. 4

from matplotlib import pyplot as plt

x = [2014,2015,2016,2017,2018,2019]
y = [50,99,120,150,270,300]
x2 = [2014,2015,2016,2017,2018,2019]
y2 = [55,150,160,200,250,295]
plt.plot(x,y,'g',label='Army (BTS FANS)', linewidth=1)
plt.plot(x2,y2,'y',label='EXO-L (EXO FANS)',linewidth=1)
plt.title('BTS VS EXO')
plt.ylabel('Jumlah Penggemar')
plt.xlabel('Tahun')
plt.legend()
plt.grid(True,color='k')
plt.show()

# In[8]: Jawaban No. 5

import numpy as np
import matplotlib.pyplot as plt
 
t = np.arange(0.0, 9.0, 1)
s = [1,2,3,4,5,6,7,8,9]
 
for i in range(1, 10):
    plt.subplot(3,3,i)
    plt.xticks([]), plt.yticks([])
    plt.title('subplot(1,2,'+str(i)+')')
    plt.plot(t,s,'-y')
 
plt.show()

# In[5]: Jawaban No. 7

import matplotlib.pyplot as plt
orang = [11,22,16,9,10,15,22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48,50,29,14,68]
umur = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(orang, umur, histtype='bar', rwidth=0.8)
plt.xlabel('Umur')
plt.ylabel('Jumlah Orang')
plt.title('Histogram')
plt.show()

# In[6]: Penanganan Error

from matplotlib import pyplot as plt

def tryExceptError():
    try:
        a=[1,2,3]
        y=[5,2,4]        
        plt.plot(x,y)        
        plt.show()        
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()

# In[7]: Main

bar = __import__('1174069_bar')
scat = __import__('1174069_scatter')
pie = __import__('1174069_pie')
plot = __import__('1174069_plot')

bar.bar()
scat.scatter()
pie.pie()
plot.plot()