from dataclasses import dataclass
from ursina import *

@dataclass
class Parameters:
    tick_distance: float

    wavelength: float
    brightnessFactor: float

    occluder: set[Vec2]

    resolution: int

    visualizerAmount: int

    detectorResolution: int
    detectorDistance: float

