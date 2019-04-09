from matplotlib import pyplot as plt
import numpy as np
def plot(a): 
    if a == 4:
        x = [1,2,3,4,5]
        y = [2,3,6,5,7]     
        x1 = [10,23,22,11,25,22,17,12,15,18]
        y1 = [23,22,25,24,21,22,26,29,11,16]
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [11,12,13,14,15,16,17,18,19,20]
        x3 = [2,4,6,8,10,12,14,16,18,20]
        y3 = [12,13,15,16,17,18,19,20,21,24]
        plt.subplot(221)
        plt.plot(x,y)
        plt.subplot(222)
        plt.plot(x1,y1)
        plt.subplot(223)
        plt.plot(x2,y2)
        plt.subplot(224)
        plt.plot(x3,y3)
        plt.show()
    elif a == 3:
        x = [1,2,3,4,5]
        y = [2,3,6,5,7]     
        x1 = [10,23,22,11,25,22,17,12,15,18]
        y1 = [23,22,25,24,21,22,26,29,11,16]
        x2 = [1,2,3,4,5,6,7,8,9,10]
        y2 = [11,12,13,14,15,16,17,18,19,20]
        plt.subplot(221)
        plt.plot(x,y)
        plt.subplot(222)
        plt.plot(x1,y1)
        plt.subplot(223)
        plt.plot(x2,y2)
        plt.show()
    elif a == 2:
        x = np.random.randint(0, 10, 10)
        y = np.random.randint(0, 10, 10)
        x1 = np.random.randint(10, 20, 10)
        y1 = np.random.randint(10, 20, 10)
        plt.subplot(211)
        plt.plot(x,y)
        plt.subplot(212)
        plt.plot(x1,y1)
        plt.show()
    elif a == 1:
        x = np.random.randint(0, 10, 10)
        y = np.random.randint(0, 10, 10)
        x1 = np.random.randint(10, 20, 10)
        y1 = np.random.randint(10, 20, 10)
        plt.subplot(111)
        plt.plot(x,y)
        plt.show()
    else:
        print("Data tidak Valid")
        
# Memanggil Function 
npm = input("Masukkan NPM Anda: ")
b = int(npm)%3+2
print(b)

if b == 4:
    plot(4)
elif b == 3:
    plot(3)
elif b == 2:
    plot(2)
elif b == 1:
    plot(1)
else:
    print("Data tidak Valid")