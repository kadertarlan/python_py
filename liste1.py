#!/usr/bin/env python
# -*- coding: utf-8 -*-

liste_tek=[]
liste_cift=[]

sayi=len(liste_tek)+len(liste_cift)

while sayi < 9:
   try:
       sayi=len(liste_tek)+len(liste_cift)
       eleman=int(raw_input("sirayla 10 adet sayi girin:"))
       z=eleman in liste_tek
       t=eleman in liste_cift
       if z== True or t==True:
           print "bu sayıyı saha önce girmiştiniz"
       elif eleman%2==0:
           liste_cift.append(eleman)
       elif eleman%2!=0:
           liste_tek.append(eleman)
   except ValueError:
       print "lütfen bir rakam girin!"

print ("girdiğiniz cift sayilar %s") %liste_cift
print ("girdiğiniz tek sayilar %s") %liste_tek
