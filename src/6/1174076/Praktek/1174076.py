
# Jawaban Nomor 2
# 1. Mengimport library matplotlib & pyplot yang diberi nama pt
from matplotlib import pyplot as pt

# 2. Mendeklarasikan variabel x dan y
x = [1,2,3]
y = [4,5,2]
# 3. Deklarasikan pt.plot yang berisi variabel
pt.plot(x,y)
pt.show()

# Jawaban Nomor 3
#Plot
from matplotlib import pyplot as garis
x = [9,3,2]
y = [4,3,1]
garis.plot(x,y, label = 'Garis', linewidth=5)
garis.legend()
garis.show()
# Bar
from matplotlib import pyplot as batang
x = [1]
y = [4]
batang.bar(x, label = 'Bar 1', height=1)
batang.bar(y, label = 'Bar 2',height=2)
batang.legend()
batang.show()
# Histogram
from matplotlib import pyplot as kotak
x = [22,26,45,39,67,25,89,10,11,35,56,67,70,63,52,78]
binds = [0,20,40,60,80,100]
kotak.hist(x, label='Histogram',rwidth=0.8)
kotak.legend()
kotak.show()

# Jawaban Nomor 4
# 1. Mengimport pyplot yang diberi nama plt
from matplotlib import pyplot as plt
# 2. Mendeklarasikan variabel x dan y
x = [9,3,2]
y = [4,3,1]
# 3. Mendeklarasikan plt.plot dengan deklarasi variabel
plt.plot(x,y, label = 'Garis Legend', linewidth=5)
# 4. Tambahkan Legend yang berfungsi untuk menambahkan informasi
plt.legend()
# Memanggil plt
plt.show()

# Jawaban 5
# Subplot
# Deklrasi varibael
x = [1,2,3,4,5]
y = [6,7,8,9,10]
#tinggi,lebar,urutan
plt.subplot(331)
plt.plot(x, y)
plt.subplot(332)
plt.bar(x, y)
plt.subplot(333)
plt.hist(x, 2)
plt.subplot(334)
plt.scatter(x, y)
plt.subplot(335)
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