# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:00:43 2022

@author: Itsmr
"""

class Dog:
    def __init__(self, fur_color, height, eye_size):
        self.__fur_color= fur_color
        self.__height= height
        self.__eye_size = eye_size
    def set_fur_color(self, fur_color):
        self.fur_color= fur_color
    def set_height(self, height):
        self.height= height
    def set_eye_size(self, eye_size):
        self.eye_size= eye_size
    def get_fur_color(self):
        return self.__fur_color
    def get_height(self):
        return self.__height
    def get_eye_size(self):
        return self.__eye_size