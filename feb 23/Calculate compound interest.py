# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 03:24:32 2020

@author: Venu
"""

#Program to enter P, T, R and calculate compound interest

P = float(input("Enter the priciple amount:"))
T = float(input("Enter the time in years:"))
R = float(input("Enter the rate of interest:"))
CIfuture = P * (pow((1 + R / 100) , T))
print("Compound interest:", CIfuture)
