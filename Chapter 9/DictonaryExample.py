# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:53:01 2022

@author: Itsmr
"""
dictionary={}
randomnum=int(input("enter a random number: "))
for k in range(randomnum):
    key = input("Enter a car: ")
    model = input("Enter  a model: ")
    dictionary[key] = model
    
print(dictionary)
    
