# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:00:12 2024

@author: Dyy
"""

h = int(input("Nhap so gio: "))
m = int(input("Nhap so phut: "))
s = int(input("Nhap so giay: "))

hs = h*3600
ms = m*60
tgi = hs+ms+s

print("{0}h{1}p{2}s".format(h,m,s))
print("Doi thanh giay la: ",tgi)