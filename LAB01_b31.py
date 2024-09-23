# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:12:29 2024

@author: Dyy
"""

a = int(input("Nhap so nguyen duong A: "))
b = int(input("Nhap so nguyen duong B: "))
c = int(input("Nhap so nguyen duong C: "))

if a+b>c or a+c>b or b+c>a:
    if a==b or a==c or b==c:
        print("Tam giac can")
    elif a==b==c:
        print("Tam giac deu")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2 :
        print("Tam giac vuong")
        if a==b or a==c or b==c:
            print("Tam giac vuong can")
    else: 
        print("Tam giac thuong")
else:
    print("Khong la tam giac")