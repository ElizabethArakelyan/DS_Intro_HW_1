# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:45:35 2022

@author: eliza
"""

def convert(x1,x2):
    hours_x1=0
    minuts_x1=0
    if isinstance(x1, float):
        hours_x1=type(int(x1))
        hours_x1=hours_x1*3600
        minuts_x1=x1-type(int(x1))
        minuts_x1=minuts_x1*60
    elif isinstance(x1, int):
        hours_x1=x1*3600
    calc=hours_x1+minuts_x1+(x2*60)
    return calc

print(convert(2,3))