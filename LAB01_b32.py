# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:21:35 2024

@author: Dyy
"""

d = float(input("Nhap so quang duong (km): "))
if d==1:
    m = 15000
elif 1<d<=5:
    m = 15000 + (d-1)*13500
elif 6<=d:
    m = 15000 + 13500*4 + (d-5)*11000
elif m>120:
    m = (15000 + 4*13500 + (d-5)*11000)*0.9
print("So tien phai tra: ",m)