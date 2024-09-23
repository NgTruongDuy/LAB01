# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:30:32 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
s=0
for i in range (0,n+1):
    s+=(2*i+1)/(2*i+2)
print(s)