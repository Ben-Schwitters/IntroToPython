# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:33:00 2022

@author: Itsmr
"""

game=input("Do you want to play a game: ")

if(game=="yes"):
    num=int(input("guess a number from 1-50: "))
    if(num==6):
        print("You have won a car ")
    elif(num >=1 and num <6 or num >6 and num<12):
        print("You were very close so you have won $20 ")
    else:
        print("You did not guess the value , goodbye ")
else:
    print("Goodbye then ")
    