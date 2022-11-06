from typing import Callable, List

from ursina import *
from ursina.prefabs.file_browser import FileBrowser

import parameters


def getParameters():
    return parameters.SoftInstance


def setParam(self, name: str, value):
    print(f"Setting {name} to {value}")

    # This throws an error if the parameter doesn't exist (member doesn't exist)
    old = getattr(getParameters(), name)

    # Ensure the given value is an alright type
    if not isinstance(value, type(value)):
        raise TypeError(f"To set {name} of parameters, it must be of the same type as {old} (current value)")

    setattr(getParameters(), name, value)


class ParametersPanel(WindowPanel):

    def simulate(self):
        getParameters().printToConsole()
        self.simulateFunction()

    def __init__(self, simulateFunction: Callable):
        """
        simulateFunction: function that will be called when the simulate button is called
        """

        self.simulateFunction = simulateFunction

        # UI elements:

        self.wavelength = Slider()
        self.wavelength.on_value_changed = lambda: self.setParam("wavelength", self.wavelength.value)

        self.brightness = Slider()
        self.brightness.on_value_changed = lambda: self.setParam("brightnessFactor", self.brightness.value)

        self.tick = Slider()
        self.tick.on_value_changed = lambda: self.setParam("tick_distance", self.tick.value)

        # Dropdowns is just a glorified button selection, not choose an entry from a list...
        """
        # This is for the occluder selection
        masks: List[DropdownMenuButton] = list()
        for fileName in os.listdir("images"):
            if re.search(".+\\.(jpeg|jpg|png)$", fileName, re.IGNORECASE) is not None:
                masks.append(DropdownMenuButton(fileName))
                print(f"Found occluder mask: {fileName}")

        self.occluder = DropdownMenu("Slit Mask", buttons=masks)
        self.occluder.on_click = lambda: self.setParam("occluder", Image.open("image/image1"))
        """

        self.occluder = FileBrowser(file_types=[".jpeg", ".jpg", ".png"], start_path=Path("images").resolve())

        self.simulate = Button(text="Run Simulation")
        self.simulate.on_click = lambda: getParameters().printToConsole()



        super().__init__(title="Simulation Parameters", content=(
            Text("Wavelength"),
            self.wavelength,
            Text("Brightness Factor"),
            self.brightness,
            Text("Tick Distance"),
            self.tick,
            self.occluder,
            self.simulate
        ))
