# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:14:13 2024

@author: Dyy
"""

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
if a<0 or b<0:
    print("Khong hop le")
else:
    cld = a%b
    cln = a//b
    print("Chia lay du cua a,b: ", cld)
    print("Chia lay nguyen cua a,b: ", cln)