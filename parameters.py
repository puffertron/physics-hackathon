from dataclasses import dataclass

from ursina import Vec2


@dataclass
class Parameters:
    tick_distance: float = 1

    wavelength: float = 500
    brightnessFactor: float = 1

    occluder: set[Vec2] = frozenset([Vec2(0, 0)])

    visualizerAmount: int = 2

    detectorDistance: float = 3

    lowResolution: int = 64  # For all planes in time simulation
    highResolution: int = 128  # For all planes in final state simulation
