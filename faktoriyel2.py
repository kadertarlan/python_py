#!/usr/bin/env  python
# -*- coding: utf-8 -*-

def acilis():
	global faktoriyel, permut, komb
	print "\n"
	print "Hoşgeldiniz\n"
	print "(1)Faktoriyel Hesaplama\n"
	print "(2)Permutasyon Hesaplama\n"
	print "(3)Kombinasyon Hesaplama\n"
	print "(4)Yardım\n"
	secim=raw_input("İşlem Seçin(1-2-3):   ")
	print "\n"
	if secim not in ["1","2","3","4"]:
		print "Geçersiz Seçim. Lütfen Yardım için seçim ekranında 4 tuşuna basın"
		acilis()
	
	if secim=="1":
		e=int(raw_input("Faktoriyel Hesapmalama için sayı girin:  "))
		fakt(e)
		print "\n"
		print "_ "*10,"\n"
		print str(e)+"! = ",faktoriyel
		print "_ "*10
		print "\n"
		acilis()
	
	if secim=="2":
		f=int(raw_input("İlk Sayıyı Girin:   "))
		c=int(raw_input("İkinci Sayıyı Girin:   "))
		if f>c:	
			perm(f,c)
			print "\n"
			print "_ "*10,"\n"
			print "P("+str(f)+","+str(c)+") = ",permut
			print "_ "*10
			print "\n"
			acilis()
		else:
			print "Geçersiz İşlem. Lütfen Yardım İçin Seçim Ekranında 4 Tuşuna Basın!"
			print "\n"
			acilis()
			
	if secim=="3":
		a1=int(raw_input("Birinci Sayıyı Girin:  "))
		a2=int(raw_input("İkinci Sayıyı Girin:   "))
		if a1>a2:
			komb(a1, a2)
			print "\n"
			print "_ "*10,"\n"
			print "C("+str(a1)+","+str(a2)+") = ",komb
			print "_ "*10
			print "\n"
			acilis()
		
		else:
			print "Geçersiz İşlem. Lütfen Yardım İçin Seçim Ekranında 4 	Tuşuna basın!"
			print "\n"
			acilis()
				
def fakt(i):
	global faktoriyel
	a=1
	k=1
	while a<i:
		k=a*k
		a=a+1
		if a==i:
			faktoriyel=a*k
	
def perm(l,n):
	global faktoriyel, permut
	lfakt=0
	nfakt=0
	fakt(l)
	lfakt=faktoriyel
	faktoriyel=1
	fakt(l-n)
	nfakt=faktoriyel
	permut=lfakt/nfakt
	
def komb(y,z):
	global permut, komb, faktoriyel
	perm(y,z)
	fakt(z)
	komb=permut/faktoriyel
		
print "\n"*3
acilis()