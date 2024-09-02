# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:41:11 2024

@author: Dyy
"""

def docso(nb):
    sv = ["Khong", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]
    if 0 <= nb <=9:
        return sv[nb]
    else:
        return "Khong doc duoc"
n = int(input("Nhap so: "))
kq = docso(n)
print(kq)