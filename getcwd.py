#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

mevcut_dizin=os.getcwd()
if mevcut_dizin=="/home/kader/Desktop/python":
    for i in os.listdir(mevcut_dizin):
         print i
    
else:
    print "Bu program yalnızca /home/istihza/Desktop \
    dizininin içeriğini gösterebilir!"
print mevcut_dizin
