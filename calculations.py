import math

"""
using variables from parameter file

"""


# distance calculation
def distance(dx: float, dy: float, dz: float) -> float:
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


# angle calculation
def angle(wavelength: float, distance: float) -> float:
    return (distance % wavelength) / wavelength * 2 * math.pi


# Calculation for wave amplitude
def amplitude(dz: float) -> float:
    return 1 / distance * (1 + (dz / distance))


# Calculating pixel color values
def cartesian(amplitude: float, angle: float) -> tuple:
    x = amplitude * math.cos(angle)
    y = amplitude * math.sin(angle)
    return (x, y)
