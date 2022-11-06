from dataclasses import dataclass
from PIL import Image

SoftInstance = None
Instance = None

@dataclass
class Parameters:
    tick_distance: float = 1

    wavelength: float = 5
    brightnessFactor: float = 1000000000000 #Turn up to make brighter pixels, will probably need to be a few hundred or more to see anything

    occluder: Image = Image.open("images/2slit.png")

    visualizerAmount: int = 3

    detectorDistance: float = 10

    lowResolution: int = 64  # For all planes in time simulation
    highResolution: int = 128  # For all planes in final state simulation
    

    def printToConsole(self):

        print()
        for attr in dir(self):
            if not attr.startswith("__") and not attr == "printToConsole":
                print(f"{attr}: {getattr(self, attr)}")

        print()


def initParams():
    global SoftInstance, Instance

    if SoftInstance is None:
        SoftInstance = Parameters()

    if Instance is None:
        Instance = Parameters()
