#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

liste=[1,2,3,4,5,6]
sayac=1
zar1=random.choice(liste)
zar2=random.choice(liste)

while zar1!=6 and zar2!=6:
    zar1=random.choice(liste)
    zar2=random.choice(liste)
    sayac=sayac+1

print  sayac, " . seferde düşeş yaptın.. tebrikler.."



