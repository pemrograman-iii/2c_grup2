# -*- coding: utf-8 -*-
"""
Chapter 4

author: D. Irga B. Naufal Fakhri.
"""
import pandas

def readpanda(namafile):
    df = pandas.read_csv(namafile)
    print(df)

readpanda('1174066.csv')

def readpandadict(namafile):
    df = pandas.read_csv(namafile).to_dict()
    print(df)

readpandadict('1174066.csv')


def readrubahtanggal(namafile):
    df = pandas.read_csv(namafile, index_col='npm', parse_dates=['tanggallahir'])
    print(df)

readrubahtanggal('1174066.csv')    

def changeindex(namafile):
    df = pandas.read_csv(namafile, index_col='npm')
    print(df)

changeindex('1174066.csv')


def renamekolom(namafile):
    df = pandas.read_csv(namafile, header=0, names=['Nomor Induk Mahasiswa', 'Nama Lengkap','Kelas dan Jurusan', 'Tanggal Lahir'])
    print(df)
   
renamekolom('1174066.csv')


def writepanda(namafile):
    df = pandas.read_csv(namafile, 
            index_col='npm', 
            parse_dates=['tanggallahir'],
            header=0, 
            names=['npm', 'nama', 'kelas', 'tanggallahir'])
    df.to_csv('1174066_edit.csv')
writepanda('1174066.csv')