#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#Finds volume of sphere by using a principle of integration (cylinders)
def sphereCalc(beginning,end,interval):
    
    if beginning >= end:
        return 0
    
    point = math.sqrt(1-beginning**2)
    
    return math.pi*(point**2)*interval + sphereCalc(beginning+interval, end, interval)
    
print(sphereCalc(-1,1,0.001))
print((4/3)*math.pi)