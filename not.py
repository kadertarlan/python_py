# !/usr/bin/env python
# -*- coding: cp1254 -*-
alinannot1=int(raw_input("notunuzu girin:"))
alinannot2=int(raw_input("ikinci notunuzu girin:"))
if alinannot1 <0 or alinannot1>100 or alinannot2<0 or alinannot2>100:
    print "gecersiz bir not.."
else:
    ortalama=(alinannot1 + alinannot2)/2
    if ortalama <=100:
        karnenotu =5
    if ortalama <85:
        karnenotu =4
    if ortalama <70:
        karnenotu =3
    if ortalama < 55:
        karnenotu =2
    if ortalama < 45:
        karnenotu =1

print "ortalamanız:",ortalama
print "karnenotunuz:",karnenotu

