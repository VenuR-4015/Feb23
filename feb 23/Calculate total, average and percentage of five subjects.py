# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 03:15:16 2020

@author: Venu
"""

#Program to enter marks of five subjects and calculate total, average and percentage

english = float(input("Enter the english marks:"))
maths = float(input("Enter the maths marks:"))
science = float(input("Enter the science marks:"))
social = float(input("Enter the social marks:"))
history = float(input("Enter the history marks:"))
total = english + maths + science + social + history
average = total / 5
percentage = (total/500)*100
print("total marks:", total)
print("average:", average)
print("percentage:", percentage)
