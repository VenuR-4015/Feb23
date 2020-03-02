# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 02:41:51 2020

@author: Venu
"""

#Program to enter two angles of a triangle and find third angle

a = int(input("Enter the first angle:"))
b = int(input("Enter the second angle:"))
c = 180 - (a+b)
print("third angle:", c)
