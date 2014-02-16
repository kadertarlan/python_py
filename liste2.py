#!/usr/bin/env python
# -*- coding: utf-8 -*-

def deneme():
     rehber=[]
     while len(rehber)<5:
          x=raw_input("isminiz:")
          y=raw_input("soyisminiz:")
          z=raw_input("telefon numaranız:")
          if x== "" or y== "" or z=="":
              pass
          else:
              rehber.append( x + " " + y + " " + z)
          print rehber

deneme() 
