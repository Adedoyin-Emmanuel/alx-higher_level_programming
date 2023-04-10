#!/usr/bin/python3
#@author: Adedoyin Emmanuel Adeniyi, @cohort11

"""
This function returns True or False if it matches the int or float type.
It takes 2 parameters and returns a boolean
"""
def matchType(a,b):
    if(type(a) == int or type(a) == float or type(b) == int or type(b) == float):
        return True
    else:
        return False
        

"""
This function adds 2 integers together
It takes 2 parameters and returns an integer
"""
# a function that adds 2 integers
def add_integer(a, b = 98):
   
    if(matchType(a,b)):
        if(type(a) == float or type(b) == float):
           return (int(a) + int(b))
        else:
           return (a + b)
    else:
        raise TypeError(" a must be an integer or b must be an integer")

        
       
    