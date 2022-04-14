# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:01:42 2022

@author: Itsmr
"""
num=40

for i in range(0,10):
    #print(num, "\n")
    num += 1
    print(num, "\n")
    print(i)

print("--------------------------")
    
for number in range (2,10,2):
    print(number)
    
    print("\n")

for num in [1,2,3,4]:
    print(num, "\n")

print("-------------------------------")

for num in range(5):
    print(num, "\n")

for num in range(4 ,25 ,3):
    print(num, "\n")
    
    if (num== 16):
        print("Error Will Robinson ")
        continue
        #break

#print in reverse order

for numbers in range (6,0,-1):
    print(numbers)
    
#User controlled loops
end = int(input("Enter a number, and I will display it's squared value:"))
print("Number\tSquare")
print("--------------")
for number in range(1, end +1):
    square = number ** 2
    print(f"{number}\t\t {square}")
    
print("--------------------------")

funny_word = "Badmamajama"
for letter in funny_word:
    print(letter)
    print(funny_word)

print("------------------------------")

for num in [1,5,8,12,15]:
    print(num)

print("-------------------")

for name in ["Carl", "Sally", "Mike"]:
    print(name)

print("------------------------------")
    
myList =[1,5,8,14]

for myList, i in enumerate(myList):
    print(myList,i)
    