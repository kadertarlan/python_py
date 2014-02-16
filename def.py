# -*- coding: utf-8 -*-

def tek():
     print "girdiginiz sayi tektir"

def cift():
     print "girdiginiz sayi ciftir."

sayi=raw_input("liutfen bir sayi girin:")
if(int(sayi)%2==0):
     cift()
else:
     tek()
