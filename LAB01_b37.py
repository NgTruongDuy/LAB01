# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:54:40 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
s=0
for i in range (1,n+1):
    if i%2==0:
#for i in range (2,n+1,2)
        s+=i
print(s)