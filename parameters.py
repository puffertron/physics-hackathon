from dataclasses import dataclass

from PIL.Image import Image

SoftInstance = None
Instance = None

@dataclass
class Parameters:

    # Generally all of these default values aren't used for the simulation. They are only used to verify the types of
    # values that are inserted into it by the GUI

    tick_distance: float = 0.5 #This is also in pixels, in simulation it doesn't look like it because z is skewed (already a TODO elesewhere to fix it)

    wavelength: float = 0.001 #Also in pixels haha, every length unit is in pixles
    brightnessFactor: float = 1000 #Turn up to make brighter pixels, will probably need to be a few hundred or more to see anything

    occluder: Image = Image.open('images/2slit.png')

    visualizerAmount: int = 7
    
    detectorDistance: float = 2000

    detectorDistance: float = 10

    lowResolution: int = 16 # For all planes in time simulation



    def printToConsole(self):

        print()
        for attr in dir(self):
            if not attr.startswith("__") and not attr == "printToConsole":
                print(f"{attr}: {getattr(self, attr)}")

        print()


def copy(p: Parameters) -> Parameters:
    return Parameters(
        tick_distance=p.tick_distance,
        wavelength=p.wavelength,
        brightnessFactor=p.brightnessFactor,
        occluder=p.occluder.copy(),
        visualizerAmount=p.visualizerAmount,
        detectorDistance=p.detectorDistance,
        lowResolution=p.lowResolution
    )


def initParams():
    global SoftInstance, Instance

    if SoftInstance is None:
        SoftInstance = Parameters()

    if Instance is None:
        Instance = Parameters()
