# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:50:32 2022

@author: Itsmr
"""

usernum= int(input("enter a number: "))
num= usernum % 2
if( num > 0 ):
   print(num)
else:
   print("there is no remander")