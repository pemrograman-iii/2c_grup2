# -*- coding: utf-8 -*-
"""
Tugas Chapter 6 Teori

@author: D. Irga B. Naufal Fakhri
"""
#%% Pemanggilan Bar
import l1174066_bar as bar

npm = input("Masukkan NPM Anda: ")
modnpm = int(npm)%3+2
print(modnpm)

if modnpm == 3:
    bar.bar(3)
elif modnpm == 2:
    bar.bar(2)
elif modnpm == 1:
    bar.bar(1)
else:
    print("Data tidak Valid")

#%% Pemanggilan Scatter
import l1174066_scatter as scatter

npm = input("Masukkan NPM Anda: ")
modnpm = int(npm)%3+2
print(modnpm)

if modnpm == 3:
    scatter.scatter(3)
elif modnpm == 2:
    scatter.scatter(2)
elif modnpm == 1:
    scatter.scatter(1)
else:
    print("Data tidak Valid")

#%% Pemanggilan Pie
import l1174066_pie as pie

npm = input("Masukkan NPM Anda: ")
modnpm = int(npm)%3+2
print(modnpm)

if modnpm == 3:
    pie.pie(3)
elif modnpm == 2:
    pie.pie(2)
elif modnpm == 1:
    pie.pie(1)
else:
    print("Data tidak Valid")
    
#%% Pemanggilan Plot
import l1174066_plot as plot

npm = input("Masukkan NPM Anda: ")
modnpm = int(npm)%3+2
print(modnpm)

if modnpm == 3:
    plot.plot(3)
elif modnpm == 2:
    plot.plot(2)
elif modnpm == 1:
    plot.plot(1)
else:
    print("Data tidak Valid")