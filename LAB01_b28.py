# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:33:33 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
for i in range (1,n+1):
    if n%i == 0:
        print("Uoc so cua N: ", i)