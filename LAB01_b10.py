# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:25:41 2024

@author: Dyy
"""

def tsnx(sx):
    tg = 0
    while sx >0:
        chs = sx%10
        tg += chs
        sx //= 10
    sonut = tg%10
    return sonut
sx = int(input("Nhap so xe gom 4 chu so: "))
kq = tsnx(sx)
print("Tong so nut cua so xe la: ", kq)