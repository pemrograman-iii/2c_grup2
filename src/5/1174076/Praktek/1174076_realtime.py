# Jawaban Nomor 1 
import serial

def getData():
    ser = serial.Serial('COM5',9600)
    print(ser.readline().decode("utf-8").strip('\n').strip('\r'))

getData()


# Jawaban nomor 3
import csv

def writeCsv():
    ser = serial.Serial('COM5',9600)
    with open('ujicoba.csv', mode='w') as csv_file:
        fieldnames = ['angka']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        while (1):
            data = ser.readline().decode("utf-8").strip('\n').strip('\r')
            writer.writerow({'angka': data})
            
writeCsv()