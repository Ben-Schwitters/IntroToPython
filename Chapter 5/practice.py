# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:40:19 2022

@author: Itsmr
"""

def cat(c):
    print(f'you heard {c} cats')
def dog(d):
    print(f'you heard {d} dogs')
    

def main():
    sound=input("what sound did you hear: ")
    if(sound=="meow"):
        num=int(input("How many did you hear: "))
        cat(num)
    elif(sound=="wolf wolf"):
        num=int(input("How many did you hear: "))
        dog(num)
    
if __name__ =='__main__':
    
    main()