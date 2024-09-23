# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:51:17 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
s=0
for i in range (1,n+1):
    s+=i
print(s)