#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=3
b=4
if a==b:
   print " a ile b birbirine eşittir."
else:
   print a,"  ile" ,b, " esit değil."

parola="python"
cevap=raw_input( "lutfen parola girin:")
if cevap==parola:
   print " parola onaylandı!"
else:
   print " parola yanlış."

isim=raw_input (" senin ismin ne:")
if isim=="kader":
   print " dogru isim"
elif isim=="tarlan":
   print " bu soyadın"
else:
   print isim ,"yanlış isim"

sayi=int(raw_input(" sayiyi gir:"))
if sayi%2!=0:
   print " sayi tektir"
elif sayi==0:
   print "sayi sıfırdır."
elif sayi%2==0:
   print " sayi cifttir"
