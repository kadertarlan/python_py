#!/usr/bin/env python
#-*- coding:utf-8 -*-

def fonksiyon(sayi):
    fak=1
    for i in range(sayi):
        fak=fak*(i+1)
    return fak
print fonksiyon(4)
