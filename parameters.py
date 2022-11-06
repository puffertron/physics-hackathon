from dataclasses import dataclass
from PIL import Image

Instance = None

@dataclass
class Parameters:
    tick_distance: float = 1

    wavelength: float = 500
    brightnessFactor: float = 1

    occluder: Image = Image.open("images/2slit.png")

    visualizerAmount: int = 3

    detectorDistance: float = 3

    lowResolution: int = 64  # For all planes in time simulation
    highResolution: int = 128  # For all planes in final state simulation
    
    brightnessFactor:float = 1 #Turn up to make brighter pixels, will probably need to be a few hundred or more to see anything


def initParams():
    global Instance
    Instance = Parameters()

