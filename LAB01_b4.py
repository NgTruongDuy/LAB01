# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:19:32 2024

@author: Dyy
"""

n = int(input("Nhap so nguyen duong 2 chu so: "))

if n>=10 and n<=99:
    pd = n%10
    pn = n//10
    s = pd+pn
    print("Tong cac chu so cua N: ", s)
else:
    print("Khong hop le")