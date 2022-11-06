import math
from ursina import Vec2
"""
using variables from parameter file

"""


# distance calculation
def distance(dx: float, dy: float, dz: float) -> float:
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


# angle calculation
def angle(wavelength: float, dist: float) -> float:
    return (dist % wavelength) / wavelength * 2 * math.pi


# Calculation for wave amplitude
def amplitude(distz: float, dist: float) -> float:
    return 1 / dist * (1 + (distz / dist))


# Calculating pixel color values
def cartesian(dz: float, dist: float, wavelength: float) -> Vec2:
    amp = amplitude(dz, dist)
    ang = angle(wavelength, dist)
    x = amp * math.cos(ang)
    y = amp * math.sin(ang)
    return Vec2(x,y)



