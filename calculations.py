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
def cartesian(amp: float, ang: float) -> Vec2:
    x = amp * math.cos(ang)
    y = amp * math.sin(ang)
    return Vec2(x,y)

printf(cartesian(amplitude()))