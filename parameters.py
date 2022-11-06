from dataclasses import dataclass

from PIL.Image import Image

SoftInstance = None
Instance = None

@dataclass
class Parameters:
    tick_distance: float = 0.5 #This is also in pixels, in simulation it doesn't look like it because z is skewed (already a TODO elesewhere to fix it)

    wavelength: float = 1 #Also in pixels haha, every length unit is in pixles
    brightnessFactor: float = 10#Turn up to make brighter pixels, will probably need to be a few hundred or more to see anything

    occluder: Image = None

    visualizerAmount: int = 4

    detectorDistance: float = 10

    lowResolution: int = 16 # For all planes in time simulation

    highResolution: int = 64  # For all planes in final state simulation


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
