# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:14:16 2022

@author: eliza
"""

def my_func(x1,x2,x3):
    if x1==0 or x2==0 or x3==0:
        return "Not a number – denominator equals zero"
    if isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float):
        calc=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        return float(calc)
    else: print("Error: parameters should be float")
       
print(my_func(1.0,1.0,1.0))