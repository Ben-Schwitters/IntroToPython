# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:00:56 2022

@author: Itsmr
"""
def FileControl():
    infile=open(r'C:\Users\Itsmr\OneDrive\Desktop\FunWithFiles.txt', "r")
    line=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    print(line+line2+line3)
    infile.close()
    
    fav=input("What is your favorite movie: ")
    infile=open(r'C:\Users\Itsmr\OneDrive\Desktop\FunWithFiles.txt', "a")
    infile.write('\n'+fav)
    infile.close()
    
def main():
    FileControl()




if __name__ == '__main__':
    main()