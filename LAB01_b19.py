# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:48:15 2024

@author: Dyy
"""

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
d = int(input("Nhap d: "))

min = a
if b<min:
    min=b
if c<min:
    min=c
if d<min:
    min=d
print("So nho nhat la: ",min)