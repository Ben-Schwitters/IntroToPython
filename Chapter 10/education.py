# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:36:18 2022

@author: Itsmr
"""

class Student:
    def __init__(self, num_year, gpa, num_classes):
        self.__num_year=num_year
        self.__gpa=gpa
        self.__num_classes=num_classes
    def set_num_year(self,num_year):
        self.__num_year= num_year
    def set_gpa(self,gpa):
        self.__gpa=gpa
    def set_num_classes(self,num_classes):
        self.__num_classes=num_classes
    def get_num_year(self):
        return self.__num_year
    def get_gpa(self):
        return self.__gpa
    def get_num_classes(self):
        return self.__num_classes
        
    
class Facilty:
    def __init__(self, position, coolness, tenure):
        self.__position=position
        self.__coolness=coolness
        self.__tenure=tenure
    def set_position(self,position):
        self.__position= position
    def set_coolness(self,coolness):
        self.__coolness=coolness
    def set_tenure(self,tenure):
        self.__tenure=tenure
    def get_position(self):
        return self.__position
    def get_coolness(self):
        return self.__coolness
    def get_tenure(self):
        return self.__tenure