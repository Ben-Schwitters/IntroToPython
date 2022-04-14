# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:20:20 2022

@author: Itsmr
"""
grade_book={}
#this is the menu where you ask them if they want to add a student and if yes then goes into student and if not 
#then it prints the gradebook and stops the program 
def Menu():
    new=input("do you want to add a new student? yes or no: ")
    if(new=="yes"):
        AddStudent()
    else:
        print(grade_book)
        return
    #this asks how many grades you want and the name of the student and run a loop for you to enter you grades
    #then passes it to the grade book after its been appended to the gradelist list
def AddStudent():
    gradeList = []
    numOfGrades=int(input("How many grades do you want? "))
    name = input("Enter the name of the student: ")
    for k in range(numOfGrades):
        grades = input("Enter the grade: ")
        gradeList.append(grades)
    StudentGradeBook(name, gradeList)
    
#this takes the values from addstudent and puts them into the dictionary, then goes back into menu to get another student if needed
def StudentGradeBook(name,grade_value):
    global grade_book
    grade_book[name] = grade_value
    print(grade_book)
    Menu()

if __name__== '__main__':
    Menu()