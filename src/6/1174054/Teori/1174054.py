# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:49:54 2019

@author: Aulyardha Anindita
"""

#Langkah-langkah membuat sumbu x dan y
from matplotlib import pyplot as plt
x = [3,5,6,7]
y = [2,16,4,6]
plt.plot(x,y)
plt.title('Info Dita')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.show()

#Fungsi Bar
from matplotlib import pyplot as plt
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="Sepatu",color="b",width=0.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Tas",color="k",width=0.5)
plt.legend()
plt.xlabel("Harian")
plt.ylabel("Jumlah")
plt.title("Data Penjualan Dita")
plt.show()

#Fungsi Line
from matplotlib import pyplot as plt
x=[2,4,6]
y=[1,3,5]
plt.plot(x,y)
plt.show

#Fungsi Histogram
from matplotlib import pyplot as plt
populasi = [40,80,11,22,16,9,10,15,22,55,62,45,21,22,102,95,85,55,110,120,70,80,75,65,54,39,32,41,46,44]
angka = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(populasi, angka, histtype='bar', rwidth=0.8)
plt.xlabel('Umur')
plt.ylabel('Orang')
plt.title('Histogram Dita')
plt.show()

#Fungsi Scatter
from matplotlib import pyplot as plt
x = [1,1.5,2,2.5,3,3.5,3.6]
y = [7.5,8,8.5,9,9.5,10,10.5]
x1=[8,8.5,9,9.5,10,10.5,11]
y1=[3,3.5,3.7,4,4.5,5,5.2]
plt.scatter(x,y, label='Pengeluaran per bulan',color='b')
plt.scatter(x1,y1,label='Pemasukan per bulan',color='m')
plt.xlabel('Pengeluaran')
plt.ylabel('Pemasukan')
plt.title('Scatter Dita')
plt.legend()
plt.show()

#Fungsi Stackplot
from matplotlib import pyplot as plt
tidur = [1,2,3,4,5,6,7]  
ngampus =[7,8,6,8,7,9,10]
makan = [2,3,4,3,2,3,4]
jalan =[7,8,7,2,2,6,0]
main = [8,5,7,8,13,15,25]
plt.plot([],[],color='y', label='Tidur', linewidth=5)
plt.plot([],[],color='b', label='Ngampus', linewidth=5)
plt.plot([],[],color='c', label='Makan', linewidth=5)
plt.plot([],[],color='g', label='Jalan', linewidth=5)
plt.stackplot(tidur, ngampus,makan,jalan,main, colors=['y','b','c','g'])  
plt.xlabel('Hari')
plt.ylabel('Aktivitas')
plt.title('Stack Plot Dita')
plt.legend()
plt.show()

#Fungsi Pie
from matplotlib import pyplot as plt
Pemrograman = [1,2,3,4,5,6,7]
RPL =[7,8,6,11,7,8,9]
Jarkom = [2,3,4,3,2,7,5]
MB =[7,8,7,2,2,4,2]
SAP = [8,5,7,8,13,7,15]
slices = [7,2,2,13]
activities = ['Pemrograman','RPL','Jarkom','SAP']
cols = ['c','m','r','b']
plt.pie(slices,
  labels=activities,
  colors=cols,
  startangle=0,
  shadow= True,
  explode=(0.1,0.1,0.1,0.1),
  autopct='%1.1f%%')
plt.title('Pie Plot Dita')
plt.show()

#Subplot
x = [1,2,3,4,5,6,7,8,9,10]
y = [10,20,30,40,50,60,70,80,90,100]
plt.subplot(221)#tinggi,lebar,urutan
plt.plot(x, y, color="r")
plt.subplot(222)
plt.bar(x, y, color="g")
plt.subplot(223)
plt.hist(x, y, color="m")
plt.subplot(224)
plt.scatter(x, y, color="c")
plt.show()