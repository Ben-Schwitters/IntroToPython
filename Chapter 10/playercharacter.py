# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:51:07 2022

@author: Itsmr
"""
#makes the class playercharacter and inside it makes 3 attributes and gives theme each accessors and mutators
class PlayerCharacter:
    def __init__(self, health, armor_rating, attack_power):
        self.__health= health
        self.__armor_rating= armor_rating
        self.__attack_power = attack_power
    def set_health(self, health):
        self.__health= health
    def set_armor_rating(self, armor_rating):
        self.__armor_rating= armor_rating
    def set_attack_power(self, attack_power):
        self.__attack_power= attack_power
    def get_health(self):
        return self.__health
    def get_armor_rating(self):
        return self.__armor_rating
    def get_attack_power(self):
        return self.__attack_power
    
