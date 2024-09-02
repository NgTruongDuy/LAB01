# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:52:21 2024

@author: Dyy
"""

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

max = a
if b>max:
    max=b
if c>max:
    max=c
print("So lon nhat la: ", max)