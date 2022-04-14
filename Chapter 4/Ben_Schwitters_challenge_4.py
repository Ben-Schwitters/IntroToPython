# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:51:51 2022

@author: Itsmr
"""
accumulator=0
game=input("Do you want to play a game: ")

if(game=="yes"):
    
    num=int(input("guess a number from 1-50: "))
    accumulator += 1
    
    while (num != 6):
        
        accumulator+=1
        
        if(num != 6):
            
            num=int(input("That is not correct, please try again: "))
            continue
        
        elif(num < 1 or num > 50):
            print("Please enter a value between 1 - 50")
            num = int(input("Please enter your number: "))
            continue
        
    if(num==6):
        print("You have won a car ")
        print(accumulator)

else:
    print("Goodbye")
