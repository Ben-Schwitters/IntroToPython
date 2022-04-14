# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:54:16 2022

@author: Itsmr
"""
set1=set()
set2=set([1,2,3,4,5,6,7])
numOfValues=int(input("How many values do you want? "))
for i in range(numOfValues):
    value=int(input("what do you want the values to be? "))
    set1.add(value)
set3=set1.intersection(set2)
print(set3)
    
    