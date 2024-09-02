# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:37:28 2024

@author: Dyy
"""

def dcc(cc):
    if cc.islower():
        return cc.upper()
    else:
        return cc.lower()
cc = input("Nhap 1 chu cai bat ky: ")
ccd = dcc(cc)

print("Chu cai sau khi doi la: ", ccd)