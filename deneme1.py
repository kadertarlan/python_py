#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sayi_isle():
     sor=input(" bir sayi girin:")
     return sor

sayi=sayi_isle()

print ("girdiginiz sayi:%s" %sayi)

if sayi%2==0:
     print "giridigin sayi cift"
else:
     print "girdigin sayi tek"

print "girdiğiniz sayının karesi: %s" %sayi ** 2
print "girdiğiniz sayının küpü: %s" %sayi ** 3

