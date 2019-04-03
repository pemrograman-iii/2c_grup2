# -*- coding: utf-8 -*-
"""
Chapter 5 Praktek

author: D. Irga B. Naufal Fakhri.
"""
import serial

def PenangananError():
    try:
        ser = serial.Serial('COM3',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Ada kesalahan dalam penulisan Syntax")
    except NameError:
        print("Variable yang dimasukkan tidak ada")
    except TypeError:
        print("Ada yang salah pada type data")
    except:
        print("Sedang terjadi sebuah kesalahan")

PenangananError()