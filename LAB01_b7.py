# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:39:54 2024

@author: Dyy
"""
import math

r = float(input("Nhap ban kinh hinh tron: "))

cv = 2*math.pi*r
dt = math.pi*r*r

print("Chu vi hinh tron la: ", round(cv,3))
print("Dien tich hinh tron la: ", round(dt,3))