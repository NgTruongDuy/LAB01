# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:32:20 2024

@author: Dyy
"""

def sxtd(n):
    chuoiso = str(n)
    listso = list(chuoiso)
    listso.sort()
    chuoikq = ''.join(listso)
    return int(chuoikq)
n = int(input("Nhap so nguyen N: "))
kq = sxtd(n)
print("So co cac con so theo thu tu tang dan: ", kq)