# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:57:43 2022

@author: Itsmr
"""

def main():
    csv_file = open(r'C:\Users\Itsmr\OneDrive\Desktop\NumGradeBook.txt', 'r')
    
    lines =csv_file.readlines()
    
    csv_file.close()
    
    for line in lines:
        tokens = line.split('/t')
        
        total = 0.0
        for token in tokens:
            total+= float(token)
        average = total/len(tokens)
        print(f'Average: {average}')
        
        
if __name__=='__main__':
    main()