# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:04:06 2024

@author: Dyy
"""

m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))

if 1<=m<=12:
    if m in [1,3,5,7,8,10,12]:
        d = 31
    elif m==2:
        if (y%4==0 and y%100!=0) or y%400==0:
            d = 29
            print("Nam nhuan")
        else:
            d = 28
            print("Nam khong nhuan")
    else:
        d = 30
    print(f"thang {m}, nam {y} co {d} ngay")