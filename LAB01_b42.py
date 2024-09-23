# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:27:21 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
s=0
for i in range (1,n+1):
    s+=1/(i*(i+1))
print(s)