# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:46:00 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
if n<2:
    print("{n] khong phai so nguyen to")
for i in range (2,n):
    if n%i==0:
        print(f"{n} khong la so nguyen to")
        break
    else:
        print(f"{n} la so nguyen to")
        break