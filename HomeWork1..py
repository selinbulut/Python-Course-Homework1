# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 22:56:56 2020

@author: user
"""


values = list()


for i in range(6):
    if i<=5:
        values1 = input("Lütfen bir değer giriniz:")
        values.extend(values1)
        print(values)
    else :
        break
for i in range(values): 
        print("My value:{} and type:{}".format(values(i), type(values(i)))) 