# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:53:50 2024

@author: Dyy
"""

print("====MENU====")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("============")
c = int(input("Moi nhap lua chon: "))
print("============")

if c==1:
    print("Vay ban da chon hu tieu")
elif c==2:
    print("Vay ban da chon chao long")
elif c==3:
    print("Vay ban da chon banh canh")
elif c==4:
    print("Vay ban da chon bun rieu")
elif c==5:
    print("Vay ban da chon pho bo")
else:
    print("Khong hop le")