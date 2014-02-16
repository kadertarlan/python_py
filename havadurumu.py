#!/usr/bin/env python
# -*- coding: utf-8 -*-

soru=raw_input("Hava durumunu öğrenmek istediğin şehrin adını gir:")

cevap={"istanbul":"gökgürültülü","ankara":"yağışlı","izmir":"parçalıbulutlu","adana":"güneşli"}

print cevap.get(soru, "bu şehre ilişkin hava durumu bulunmamakta.")
