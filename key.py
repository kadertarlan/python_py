# -*- coding: utf-8 -*-

def kayit_ekle(isim, soyisim, sehir, meslek, tel, adres):
     kayit = {}
     kayit["%s %s" %(isim, soyisim)] = [sehir, meslek, tel, adres]
     print "\nBağlantı bilgileri kayıtlara eklendi!\n"
     for k, v in kayit.items():
         print k
         print "-"*len(k)
         for i in v:
             print i

isi = raw_input("isim: ")
soy = raw_input("soyisim: ")
seh = raw_input("şehir: ")
mes = raw_input("meslek: ")
tel = raw_input("telefon: ")
adr = raw_input("adres: ")

kayit_ekle(isi, soy, seh, mes, tel, adr)
