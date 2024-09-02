# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:27:24 2024

@author: Dyy
"""

a = float(input("Nhap a: "))
b = float(input("Nhap a: "))
c = float(input("Nhap a: "))

t=0
if a>b:
    t=a
    a=b
    b=t
if a>c:
    t=a
    a=c
    c=t
if b>c:
    t=b
    b=c
    c=t

print("Thu tu tang dan cac so: ", a,b,c)

def sxtd(n):
    chuoiso = str(n)
    listso = list(chuoiso)
    listso.sort()
    chuoikq = ''.join(listso)
    return int(chuoikq)
n = int(input("Nhap so nguyen N: "))
kq = sxtd(n)
print("So co cac con so theo thu tu tang dan: ", kq)