# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:52:29 2022

@author: Itsmr
"""
#Creates booleans that are false
def checkNumber(num):
    numList=[]
    hasDigitOne=False
    hasDigitTwo=False
    hasDigitThree=False
    hasDashOne=False
    hasDashTwo=False
    hasLength=False
#has multiple for loops that checks for input validation
    for numb in num:
        numList.append(numb) 
    length=len(numList)
    for c in numList[0:3]:
       if(c.isdigit()):
           hasDigitOne=True
           
    for ch in numList[3:7]:
       if(ch.isdigit()):
           hasDigitTwo=True
           
    for cha in numList[8:]:
       if(cha.isdigit()):
           hasDigitThree=True
    if(length==12):
        hasLength=True
    for char in numList:
        if(numList[3]=="-"):
            hasDashOne=True
        if(numList[7]=="-"):
            hasDashTwo=True
#checks if the digits are all true and if so then return true else return false 
    if(hasDigitOne and hasDigitTwo and hasDigitThree and  hasDashOne and hasDashTwo and hasLength ==True):
        return True
    else:
        return False
            
  #asks for the number and then if n is true it prints the phone number and if not then prints that number is wrong  
def getNumber():
    number=input("what is your phone number with dashes? ")
    n=checkNumber(number)
    if(n==True):    
        print(f'{number} is a phone number')
    else:
        print("That phone number is wrong")
    
if __name__=='__main__':
    getNumber()