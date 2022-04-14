# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:16:21 2022

@author: Itsmr
"""
GRAVITY=9.8


def fallingDistance(t):
    #distance_traveled_per_second=1
    
    for i in range (1,t+1):
        distance_traveled_per_second = (.5 *GRAVITY) * (i**2)
        print(distance_traveled_per_second)
        


def main():
    print("Hello, this program determines the distance an object has traveled while in a state of free fall.")
    time_of_fall=int(input("How long would you like the object to be falling: "))
    fallingDistance(time_of_fall)
    

if __name__ == '__main__':
    main()