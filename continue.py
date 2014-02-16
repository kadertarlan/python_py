#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
     s=raw_input("bir sayi gir:")
     if (s=="iptal"):
          break
     if len(s) <=3:
          continue
     print "en az 4 basamaklı sayi gir."
     
