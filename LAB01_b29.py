# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:24:43 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
s=0
for i in str(n):
    s += int(i)
print(s)