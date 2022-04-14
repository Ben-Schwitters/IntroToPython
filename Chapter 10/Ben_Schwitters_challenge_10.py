# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:18:06 2022

@author: Itsmr
"""
#asks the character for the values they want and keeps looping till the put the correct numbers in
#then makes an object of playercharacter and prints the values
def main():
    import playercharacter
    h=int(input("How much health would you like to have between 1-100: "))
    while h<1 or h>100:
        h=int(input("How much health would you like to have between 1-100: "))
          
    
    armor=int(input("How much armor would you like have between 1-20: "))
    while armor<1 or armor>20:
        armor=int(input("How much armor would you like have between 1-20: "))
    
    attack=int(input("How much attack would you like to have between 1-20: "))
    while attack<1 or attack>20:
            attack=int(input("How much attack would you like to have between 1-20: "))
    
    Wizard = playercharacter.PlayerCharacter(h,armor,attack)
    print(f'Your health is {Wizard.get_health()} \nYour armor is {Wizard.get_armor_rating()} \nYour attack is {Wizard.get_attack_power()}')



if __name__ == "__main__":
    
    main()
    
