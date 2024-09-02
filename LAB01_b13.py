# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:01:43 2024

@author: Dyy
"""

def ddn(ngs,ts,ns):
    a = f"{ngs}/{ts}/{ns}"
    b = f"{ngs}/{ts}/{ns:02d}"
    c = f"{ns}/{ts}/{ngs}"
    print(a)
    print(b)
    print(c)
ngs = int(input("Nhap ngay sinh: "))
ts = int(input("Nhap thang sinh: "))
ns = int(input("Nhap nam sinh: "))
ddn(ngs,ts,ns)