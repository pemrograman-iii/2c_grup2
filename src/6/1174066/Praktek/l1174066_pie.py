# -*- coding: utf-8 -*-
"""
Tugas Chapter 6 Teori

@author: D. Irga B. Naufal Fakhri
"""
#%% Nomor 3
from matplotlib import pyplot as plt

def pie(mod):
    if mod == 3:
        aktivitas= [8,1,14,2]
        game = [10,18,4]
        prog = [7,5,6,1]
        activities = ['Tidur','Makan','Kerja','Main']
        games = ['Minecraft','osu','CSGO']
        programming = ['C#','Java','PHP','HTML']
        cols = ['m','r','c','b']
        plt.subplot(221)
        plt.pie(aktivitas,
                 labels=activities,
                 colors=cols,
                 startangle=0,
                 shadow= True,
                 explode=(0.2,0,0,0),
                 autopct='%1.1f%%')
        plt.title('Pie Aktivitas')
        
        plt.subplot(222)
        plt.pie(game,
                 labels=games,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.3,0.1,0),
                 autopct='%1.1f%%')
        plt.title('Pie Gaming')
        
        plt.subplot(223)
        plt.pie(prog,
                 labels=programming,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.1,0,0,0),
                 autopct='%1.1f%%')
        plt.title('Pie Programming')
        plt.show()
    else:
        print("Data belum dimasukkan")
        