#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

if os.name=="posix":
    if os.system("mkdir 'yeni klasör' "):
        print "klasör başarılı bir şekilde oluşturuldu.."
    else:
        print " klasör oluşturulamadı.."
if os.name=="nt":
    if os.system("md yeni klasör"):
        print "klasör oluşturuldu.."
    else:
        print "klasör olusturulmadı.."

