# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 02:28:17 2020

@author: Venu
"""

#Program to convert days into year, weeks and days

days = int(input("Enter the days:"))
year = int(days / 365)
weeks = int((days - (year * 365)) / 7)
days = int(days - ((year * 365) + (weeks * 7))) 
print("year:", year)
print("weeks:", weeks)
print("days:", days)
