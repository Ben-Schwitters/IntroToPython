# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:52:32 2022

@author: Itsmr
"""
def Database(name, location, value):    
    
    saved_database = []    #WE ARE CREATING AN EMPTY LIST HERE
    
    inFile = open(r'C:\Users\Itsmr\OneDrive\Desktop\StudentGradeBook.txt', 'r')     #HERE WE ARE OPENING A FILE IN READ MODE
    
    for lines in inFile:    #WE ARE GOING TO LOOP THROUGH EVERY LINE IN THE FILE
        
        saved_database.extend(lines.split('\t'))    #WE ARE SAVING EACH ITEM SEPARATED WITH A TAB TO A LOCATION IN THE LIST

        
    print(saved_database)
    
    print('\n------------------------------')
    inFile.close()
    
    if(name in saved_database):
        nameLocation= saved_database.index(name)
        newGradeLocation=nameLocation+location
        saved_database[newGradeLocation]=value
        print(saved_database)
    else:
        print("name is not in the database")
        
        
# COMPLETE THIS SECTION USING A DECISION STRUCTURE TO SEE IF THE NAME IS CONTAINED IN THE DATABASE.  
#IF IT IS, THEN YOU MUST FIND THE INDEX VALUE AND #REPLACE THE APPROPRIATE GRADE.  
#IF THE NAME IS NOT IN THE DATABASE, TELL THE USER IT WAS NOT FOUND IN THE GRADEBOOK. 
    
    with open(r'PATH_TO_YOUR_FILEStudentGradeBook.txt', 'w') as f:       #OPEN THE FILE IN WRITE MODE
        
        for elements in saved_database:   #ITERATE THROUGH EVERY ELEMENT IN THE DATABASE
            
            f.write('%s\t' % elements)   #WRITE EACH VALUE TO THE DATABASE BACK INTO DELIMITED FORM.  
            
            
    f.close()    
    
def ChangingGrades():
    
    #This function will let the user access the working_database and change any 
    #grade contained in the function
    studentName= input("What is the name of the student you wish to access? ")
    studentGrade= int(input("What grade would you like to change? "))
    studentNewGrade= int(input("What will the new grade be? "))
    Database(studentName, studentGrade, studentNewGrade)

#YOU MUST COMPLETE THIS SECTION OF THE CODE ON YOUR OWN. DO NOT USE THE SAME NAME FOR THE VARIABLES IN THE PARAMATER FIELD OF THE  DATBASE() #FUNCTION.   
#REMEMBER YOU MUST CALL THE DATABASE FUNCTION AND PASS THE SAME NUMBER OF ARGUMENT, IN THIS CASE 3.  
#ONE FOR THE STUDENTS NAME, #ONE FOR THE GRADE NUMBER YOU ARE CHANGING, AND ONE FOR THE NEW GRADE VALUE.      

if __name__=='__main__':
    ChangingGrades()