# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:44:46 2022

@author: Itsmr
"""
baskets=0
num = 3
print("Welcome ")
while(baskets !=10):
    guess=(int(input("guess a number 1-5: ")))
    if(guess==3):
        baskets+=1
    if(baskets==10):
        break
    