#!/usr/bin/env python
# -*- coding: utf-8 -*-

meyveler = ["elma", "erik", "elma", "çilek",
            "karpuz", "kavun", "su", "elma"]

sira = 0
liste = []
while sira < len(meyveler):
    try:
        oge = meyveler.index("elma", sira)
    except ValueError:
        pass
    sira += 1
    if not oge in liste:
        liste.append(oge)

for nmr in liste:
    print "aranan öğe %s konumunda bulundu!"%nmr
