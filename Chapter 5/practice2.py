# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:44:29 2022

@author: Itsmr
"""
import math


def squareRoot(n):
    for i in range(n,0-1,-1):
        result= math.sqrt(i)
        print(result)
    
    
def main():
    num=int(input("give me number: "))
    squareRoot(num)


if __name__ =='__main__':
    
    main()