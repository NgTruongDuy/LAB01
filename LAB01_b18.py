# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:47:58 2024

@author: Dyy
"""
h1 = int(input("Nhap gio thu nhat: "))
m1 = int(input("Nhap phut thu nhat: "))
s1 = int(input("Nhap giay thu nhat: "))
h2 = int(input("Nhap gio thu hai: "))
m2 = int(input("Nhap phut thu hai: "))
s2 = int(input("Nhap giay thu hai: "))

tg1 = h1*3600 + m1*60 + s1
tg2 = h2*3600 + m2*60 + s2
tg = tg1+tg2
print("Tong 2 thoi gian: ", tg)
h = tg1-tg2
if h>0:
    print("Hieu 2 thoi gian: ", h)
else:
    print("Khong hop le")