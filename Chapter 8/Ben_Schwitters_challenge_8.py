# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:26:30 2022

@author: Itsmr
"""
def validPassword(validpass):
    bannedCharacters = ["#","$","_","-","+","="]
    hasUpper=False
    hasLower= False
    hasDigit= False
    valid= False
   #this says that if there are any banned characters in my validpass then it will make valid false
   #otherwise it will make it true
    if(any(char in bannedCharacters for char in validpass)):
        valid=False
    else:
        valid = True
    #char validation test
    for char in validpass:
         if(char.isupper()):
             hasUpper=True
         if(char.islower()):
             hasLower=True
         if(char.isdigit()):
             hasDigit=True
    
    #this says if all of the validation tests are true then it will return true and say you have a valid pass     
    if(hasUpper==True and hasLower==True and hasDigit==True and valid == True):
         print("Your password is valid ")
         return True
    else:
         print("Your password is not valid ")
         return False
         
def StoredPasswords(checkPass):
    commonPass= ["123456","123456789","12345","qwerty","password","12345678","111111","123123","1234567890","1234567",
                 "qwerty123","000000","Abcdefg123!","aa12345678","abc123","password1","1234","qwertyuiop","123321",
                 "password123","1q2w3e4r5t","iloveyou","654321","666666","987654321","123","123456a","qwe123",
                 "1q2w3e4r","7777777","1qaz2wsx","123qwe","zxcvbnm","121212","asdasd","a123456","555555","dragon",
                 "112233","123123123","money","11111111","qazwsx","159753","asdfghjkl","222222","1234qwer","qwerty1",
                 "123654","123abc"]
    #if your password is in the database after it checks it, it will says its too common and give you the index number then return it 
    #else it will print that it was not found and then will append to the list and print the list
    if checkPass in commonPass:
        found="Your password is too common. Please consider changing it. "
       
        print("index number: ",commonPass.index(checkPass))
        return found
    else:
       notfound="Your password was not found in the database Goodjob"
       commonPass.append(checkPass)
       print(commonPass)
       return notfound
    

def getUserPass():
    username= input("What will your username be? ")
    password= input("Enter a password that has one capital, one lower, one number and one special character, and is 8 characters long: ")
   #gets the length of the password and checks to see if its correct
    passLength=len(password)
    while(passLength<8):
        password= input("The password you entered wasn't 8 characters long , please enter a password that has one capital, one lower, one number and one special character, and is 8 characters long: ")
        passLength=len(password)
        #if the password meets the criteria then it goes onto valid pass
    if(passLength>=8):
        vPass=validPassword(password)
    #if the password returned true from validpass that means its a valid password and goes onto the database
    if(vPass==True):
        result=StoredPasswords(password)
        print (result)
        

if __name__=='__main__':
    getUserPass()