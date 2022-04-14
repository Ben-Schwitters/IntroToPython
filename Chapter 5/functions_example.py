# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:48:11 2022

@author: Itsmr
"""
myVariable= 5

def Greetings(n):
    
    localVariable = 10
    print(localVariable)
    newValue = n+ n
    print(newValue)
    return n
    
def newFunction():
    
    print("Get out of here")   
    #Greetings(4)

def main():
    
    print("My Planet")
    newFunction()
    Greetings(4)
    

if __name__ == '__main__':
    main()