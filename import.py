#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
kntrl = ""

while True:
    if kntrl == 'q' or kntrl== 'Q':
        break
    else:
        loto=random.sample(xrange(1,50),6)
        stopu1=random.sample(xrange(1,35),5)
        stopu2=random.sample(xrange(1,15),1)
        onnum = random.sample(xrange(1,81),10)
        sloto=random.sample(xrange(1,55),6)

        loto.sort()
        stopu1.sort()
        onnum.sort()
        sloto.sort()

        print "\n\nsayısal loto:\n%s \n" %(loto)
        print "sans topu=\n%s + %s \n" %(stopu1,stopu2)
        print "on numara:\n %s \n " %(onnum)
        print "super loto:\n%s\n " %(sloto)

        kntrl =raw_input("yeni sayılar için \"enter\" ,\
        cıkmak icin \"Q \" tusuna basın..")
