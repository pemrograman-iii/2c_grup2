# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 21:29:47 2019

@author: Chandra Kirana Poetra
"""

import serial

def tryExceptError():
    try:
        ser = serial.Serial('COM5',9600)
        print(ser.readline().decode("utf-8").strip('\n').strip('\r'))
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")
        
tryExceptError()