# -*- coding: utf-8 -*-
"""
Tugas Chapter 6 Teori

@author: D. Irga B. Naufal Fakhri
"""
def PenangananError():
    try:
        from matplotlib import pyplot as plt
    except SyntaxError:
        print("Ada kesalahan dalam penulisan Syntax")
    except NameError:
        print("Variable yang dimasukkan tidak ada")
    except TypeError:
        print("Ada yang salah pada type data")
    except:
        print("Sedang terjadi sebuah kesalahan")

PenangananError()