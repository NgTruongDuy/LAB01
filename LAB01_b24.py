# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:59:35 2024

@author: Dyy
"""

h = int(input("Nhap gio: "))
m = int(input("Nhap phut: "))
s = int(input("Nhap giay: "))

if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
    print("Thoi gian hop le")
else:
    print("Thoi gian khong hop le")