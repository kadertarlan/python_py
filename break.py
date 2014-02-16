#!/usr/bin/env python
# -*- coding: utf-8 -*-

kullaniciadi="kullanici"
parola="parola"

while True:
     soru1=raw_input("kullanıcı adınız:")
     soru2=raw_input("parola:")

     if soru1==kullaniciadi and soru2==parola:
          print " kullanıcı adınız ve parolanız doğru."
          break
     else:
          print "kullanıcı adınız ve parolanız yanlış.\n Lütfen tekrar deneyin.."

