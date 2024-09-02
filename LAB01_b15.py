# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:40:06 2024

@author: Dyy
"""

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

t1 = (a+b) / (a**(1/3) + b**(1/3))
t2 = t1 - (a*b)**(1/3)
m1 = a**(1/3) - b**(1/3)
m2 = m1**(1/2)
s = t2/m2

print("Ket qua phep toan: ", s)