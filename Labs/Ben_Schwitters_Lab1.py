# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 18:49:26 2022

@author: Itsmr
"""
pizzaCounter=0
name=input("What is your name: ")
print("Hello "+name+" Welcome to the Python Pizza chooser.")
print("There are 3 types of pizza you can choose from: cheese, pepperoni, and supreme")
choice=input("Would you like to buy pizza? ")
if(choice.lower()=="yes"):
    pizzaChoice=input("What type of pizza would you like to buy: ")
    pizzaCounter+=1
    while(choice.lower()=="yes"):
        choice=input("Would you like to buy another pizza? ")
        if(choice.lower()=="yes"):
            pizzaChoice=input("What type of pizza would you like to buy: ")
            if(pizzaChoice.lower()=="cheese" or "pepperoni" or "supreme"):
                pizzaCounter+=1
        else:
            break
'''else:
    print("Goodbye")
    '''
print("Thank you " +name+  " The "+str(pizzaCounter)+ " pizzas you ordered will be ready in 30 minutes.")
            
    
    
