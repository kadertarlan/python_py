#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
     ilk=int(raw_input("bölme işlemi için ilk sayiyi gir:"))
     ikinci=int(raw_input("lütfen ikinci sayiyi gir:"))
     sonuc=float(ilk)/(ikinci)
     print sonuc
except ZeroDivisionError:
     print "lütfen sayiyi 0 a bölmeye çalışmayın"

except ValueError:
     print "litfen bir rakam girin:"
