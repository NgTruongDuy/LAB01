# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:05:26 2024

@author: Dyy
"""

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if b>0: 
    print("{0}x + {1} = 0".format(a,b))
else:
    print("{0}x {1} = 0".format(a,b))
if a==0:
    if b==0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x = -b/a
    print("Phuong trinh co nghiem duy nhat")
    print("x = -b/a = ", x)