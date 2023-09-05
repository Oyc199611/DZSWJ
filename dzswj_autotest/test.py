# -- coding: utf-8 --
"""
@Author : oyc
@Time : 2023/9/4 21:12
"""
a = 0
for i in range(1, 101):
    a += i
    if i == 50:
        continue

print(a)
