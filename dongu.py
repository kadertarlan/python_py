#!/usr/bin/env python
# -*- coding: utf-8 -*-

a=0;
while a<3:
  a=a+1
  print a
print "\n"

for i in range(1,10):
   print i

for i in "kelime":
   print i
print "\n"
for i in range(0,11,2):
   print i
print "\n"

print range(10,15)

print range(0,20,3)


a=" kader tarlan "
print len(a)


a=1234567
b=str(a)
c=len(b)
print c
a="kader"
print 'k' in a


kul_ad="kader"
kul_soyad="tarlan"
while True:
   ad=raw_input(" kullanıcı adı:")
   soyad=raw_input( "kullanıcı soyad:")
   if ad==" " and soyad==" ":
     continue 
   if ad==kul_ad and soyad==kul_soyad:
      print " programa hosgeldınız."
      break
   else:
      print " yanlıs ad soyad"
      break
cevap=raw_input(" sistemden cıkmak mı istiyorsunuz(e/E)")
if 'e' in cevap or 'E' in cevap:
   print "gule gule"

