# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:58:43 2022

@author: Itsmr
"""


def main():
    import education
    years=2
    grade_average=4
    classes=5
    
    p="Python"
    cool="10"
    ten="no"
    
    Ben=education.Student(years,grade_average,classes)
    Teacher=education.Facilty(p, cool, ten)
    print(f'He has been in collge for {Ben.get_num_year()} years, His grade average is {Ben.get_gpa()}, He has {Ben.get_num_classes()} classes')
    
    
if __name__ == "__main__":
    
    main()