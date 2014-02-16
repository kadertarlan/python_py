#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

secenek1= "(1) toplama"
secenek2= "(2) cıkarma"
secenek3= "(3) carpma"
secenek4= "(4) bölme"
print secenek1    
print secenek2    
print secenek3    
print secenek4

secenek=int(raw_input("Lütfen seceneğini gir:"))
if(secenek==1):
     sayi1=int(raw_input("toplanacak ilk sayini gir:"))
     sayi2=int(raw_input("toplanacak ikinci sayini gir:"))
     toplam=sayi1+sayi2
     print (" %s+%s =%s " %(sayi1,sayi2,toplam))


