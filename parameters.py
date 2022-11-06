from dataclasses import dataclass
from typing import Set

from ursina import *


@dataclass
class Parameters:
    tick_distance: float = 1

    wavelength: float = 500
    brightnessFactor: float = 1

    
    occluder: Texture = Texture("images/2slit.png")
    
    visualizerAmount: int = 1

    detectorDistance: float = 3

    lowResolution: int = 64  # For all planes in time simulation
    highResolution: int = 128  # For all planes in final state simulation


def get_occlusion_holes(tex: Texture):
    holes = []
    for x in range(0, tex.width):
        for y in range(0, tex.height):
            print (tex.get_pixel(x,y).brightness)
            if tex.get_pixel(x, y).brightness < 0.5:
                #these pixels are holes
                holes.append(Vec2(x,y))
    
    return holes
