from matplotlib import pyplot as plt

def pie(a):
    if a == 4:
        aktivitas= [8,1,14,2]
        game = [10,18,4]
        prog = [7,5,6,1]
        kosan = [1,2,3,4]
        house = ['psm','kosan kaka','a','kosan boga cai']
        kegiatan = ['Tidur','Makan','Kerja','Main']
        permainan = ['Minecraft','aoe 2','CSGO']
        programming = ['C#','Java','PHP','HTML']
        cols = ['m','r','c','b']
        plt.subplot(221)
        plt.pie(aktivitas,
                 labels=kegiatan,
                 colors=cols,
                 startangle=0,
                 shadow= True,
                 explode=(0.2,0,0,0))
        plt.title('Pagawean')
        
        plt.subplot(222)
        plt.pie(game,
                 labels=permainan,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.3,0.1,0))
        plt.title('Ulin')
        
        plt.subplot(223)
        plt.pie(prog,
                 labels=programming,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.1,0,0,0))
        plt.title('Pemrogaman')
        plt.show()
        
        plt.subplot(224)
        plt.pie(kosan,
                 labels=house,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=(.1,0,0,0))
        plt.title('Kosan')
        plt.show()
    else:
        print("Data belum dimasukkan")
        
npm = input("Masukkan NPM Anda: ")
b = int(npm)%3+2
print(b)
pie(4)