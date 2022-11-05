import math
"""
using variables from parameter file

"""
PI = math.pi
#distance calculation
distance = math.sqrt(distancez ** 2 + distancex ** 2 + distancey ** 2)


angle = (distance % lambda)/lambda * 2 * PI

#Calculation for wave amplitude
amplitude = 1 / distance * (1 + (distancez / distance))

#Calculating pixel color values
red = amplitude * math.cos(angle)
blue = distance
green = aplitude * math.sin(angle)