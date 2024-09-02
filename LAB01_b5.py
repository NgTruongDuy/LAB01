# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:26:04 2024

@author: Dyy
"""

h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))

hs = h*3600
ms = m*60
tgi = hs+ms+s

print("{0}:{1}:{2}".format(h,m,s))
print("Doi thanh giay la: ",tgi)
