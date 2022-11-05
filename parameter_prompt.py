from dataclasses import dataclass
from ursina import Vec2

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


def prompt() -> Parameters:
    pass


if __name__ == "__main__":
    params: Parameters = prompt()
