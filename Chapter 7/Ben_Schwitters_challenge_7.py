# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 09:26:30 2022

@author: Itsmr
"""

def StoredPasswords(checkPass):
    commonPass= ("123456","123456789","12345","qwerty","password","12345678","111111","123123","1234567890","1234567",
                 "qwerty123","000000","1q2w3e","aa12345678","abc123","password1","1234","qwertyuiop","123321",
                 "password123","1q2w3e4r5t","iloveyou","654321","666666","987654321","123","123456a","qwe123",
                 "1q2w3e4r","7777777","1qaz2wsx","123qwe","zxcvbnm","121212","asdasd","a123456","555555","dragon",
                 "112233","123123123","money","11111111","qazwsx","159753","asdfghjkl","222222","1234qwer","qwerty1",
                 "123654","123abc")
    if checkPass in commonPass:
        found="Your password is too common. Please consider changing it. "
       
        print("index number: ",commonPass.index(checkPass))
        return found
    else:
       notfound="You have a strong password. "
     
       return notfound
    

def getUserPass():
    username= input("What will your username be? ")
    password= input("what will your password be? ")
    result=StoredPasswords(password)
    print (result)

if __name__=='__main__':
    getUserPass()