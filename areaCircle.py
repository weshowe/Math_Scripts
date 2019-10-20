# -*- coding: utf-8 -*-
import math

# Finds area of a circle by building triangles inside its component arcs.
def arc(width, height, area, counter, epsilon):
    if height <= epsilon:
        return 0
    
    else:
        area = 0.5*height*width*(2**counter)
        counter+=1
        width = math.sqrt((0.5*width)**2 + height**2)
        height = 1-math.sqrt(1-(0.5*width)**2)
        
        return area + arc(width, height, area, counter, epsilon)
    
print(2*arc(2,1,0,0,0.000000000000001))
print(math.pi)
