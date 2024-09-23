# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:32:02 2024

@author: Dyy
"""

x = int(input("Nhap so nguyen duong X: "))
n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
s=0
ts=0
ms=0
for i in range (1,n+1):
    ts = x**i
    ms += i
    s += ts/ms
print(s)