# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:08:13 2024

@author: Dyy
"""

bo_nghiem = []
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            bo_nghiem = (x,y,z)
if bo_nghiem:
    print(f"{bo_nghiem}")