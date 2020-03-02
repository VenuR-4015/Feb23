# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:55:30 2020

@author: Venu
"""

#Program to perform input/output of all basic data types 

#Integer
x = -3
print(x)
print(type(x))

#Float
y = 3.14
print(y)
print(type(y))

#Complex
z = 1+5j
print(z)
print(type(z))

#String
a = "6benches"
print(a)
print(type(a))
print(len(a))
a.upper()
a.lower()
a[1]

#List
l1 = [1,2,3,4,5]
l1[1]
l1[3]
l1[-2]
l1[:4]
l1[4:]
l1[1:4:1]
print(len(l1))
l1.append(0)

#Tuples
my_tuple = (9,6,8,0)
my_tuple[1]
my_tuple[-3]
my_tuple[1:3]

#Dictionary
dict = {1:'A', 2:'B', 3:'C'}
dict[1]
dict[2]
dict[3]

#Sets
set = {5,6,7,8}
set1 = {1,2,3,4,6}
print("Union=", set|set1)
print("Intersection=", set & set1)
print("Difference=", set-set1)

#Boolean
B1 = 'A'
B2 = 12
print(bool(B1))



































