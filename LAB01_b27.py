# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:26:17 2024

@author: Dyy
"""

import math

h = input("Nhap hinh (v: vuong, n: chu nhat, t: tron): ")
if h == 'v':
    canh = float(input("Nhap do dai canh: "))
    cv = 4*canh
    dt = canh*canh
elif h == 'n':
    cd = float(input("Nhap chieu dai: "))
    cr = float(input("Nhap chieu rong: "))
    cv = 2*cd*cr
    dt = cd*cr
elif h == 't':
    r = float(input("Nhap ban kinh: "))
    cv = 2*math.pi*r
    dt = math.pi*r*r
else:
    print("Hinh khong hop le")
print("Chu vi la: ", round(cv,3))
print("Dien tich la: ", round(dt,3))