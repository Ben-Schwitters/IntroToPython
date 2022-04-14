# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:16:09 2022

@author: Itsmr
"""

print("What is your name ")
name=input()
print("What is your birth year")
birthYear=int(input())
currentYear=2022
age=currentYear-birthYear
print("Your name is "+ name +" You were born in "+ 
str(birthYear) +". "+"That makes you approximately "+str(age)+" years old.")