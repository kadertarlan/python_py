#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
sayi=random.randrange(1,100,1)
deneme=0
print "bu bir tahmin programıdır. 1 ile 100 arasında bir sayi girin.."

while True:
    tahmin=int(raw_input("tahmininiz:"))
    
    if tahmin== sayi:
        print "\n\n Tebrikler! %s. denemede bildiniz.." %(deneme)
        break
    elif tahmin < sayi:
        print "yukarı"
        deneme=deneme+1
    elif tahmin > sayi:
        print "asaği"
        deneme=deneme+1

