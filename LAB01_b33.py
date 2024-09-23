# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:31:22 2024

@author: Dyy
"""

import math
n = int(input("Nhap so nguyen duong N: "))
while n<=0:
    n = int(input("Nhap lai so nguyen duong N: "))
scp = math.sqrt(n)
if scp == int(math.sqrt(n)):
#if math.sqrt(n) == int(math.sqrt(n)):
    print(f"{n} la so chinh phuong")
else:
    print(f"{n} khong phai so chinh phuong")