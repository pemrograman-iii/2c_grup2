#In [1] Jawaban No. 2
from matplotlib import pyplot as plt
 
x=[3,4,2]
y=[7,1,5]

plt.plot(x,y)

plt.show()

# In[2] Jawaban No. 4

from matplotlib import pyplot as plt

x = [2014,2015,2016,2017,2018,2019]
y = [74,77,100,122,64,88]
x2 = [2014,2015,2016,2017,2018,2019]
y2 = [134,97,114,134,146,167]
plt.plot(x,y,'b',label='Mahasiswa yang Tidak Hadir', linewidth=1)
plt.plot(x2,y2,'r',label='Mahasiswa yang Telat',linewidth=1)
plt.title('Kehadiran Mahasiswa')
plt.ylabel('Jumlah Mahasiswa')
plt.xlabel('Tahun')
plt.legend()
plt.grid(True,color='k')
plt.show()

# In[3]: Jawaban No. 5

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

# In[4]: Jawaban No. 7

import matplotlib.pyplot as plt
orang = [14,13,15,9,10,18,22,55,62,43,21,22,34,42,42,4,2,3,95,64,55,110,96,70,65,55,131,115,80,75,65,54,44,43,42,48,50,29,14,68]
umur = [0,10,20,30,40,50,60,70,80]
plt.hist(orang, umur, histtype='bar', rwidth=0.5)
plt.xlabel('Umur')
plt.ylabel('Jumlah Kematian')
plt.title('Histogram')
plt.show()