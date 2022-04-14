# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:51:47 2022

Exception Handling

@author: iburr
"""
#Global Variable
#result = 0

#Graceful Error Handling
def Gracefull():
    
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another nuber: "))
    
    if num_2 != 0:
        
        print(int(num_1/num_2))
        
    else:
        
        print("You cannot divide a nuber by 0.")
    

#Explicit Error Handling
def ExceptionHandling():
    
    try:
        num_1 = int(input("enter a nummber: "))
        num_2 = int(input("Enter another number: "))
        
        #local variable
        result = num_1 / num_2
        
        print(int(result))
    #also, ZeroDivisionErro as err:    
    except ZeroDivisionError:
        
        print("You cannot divide by 0")
        #print(err)
        
    #print(int(result))
    
def FileExceptions():
    try:
        infile=open(r'C:\Users\Itsmr\OneDrive\Desktop\test2.txt', "r")
        line=infile.readline()
        mynumber=line+500
        print(mynumber)
        
    except TypeError:
        print("Cannot add string literal to integer ")
    
    #to catch all errors, just use except without an error type
    

if __name__=='__main__':
    
    #Gracefull()
    #ExceptionHandling()
    FileExceptions()