from typing import Callable, List

from PIL import Image
from ursina import *
from ursina.prefabs.file_browser import FileBrowser, FileButton

import parameters
import utils


def getParameters():
    return parameters.SoftInstance


def setParam(name: str, value):
    print(f"Setting {name} to {value}")

    # This throws an error if the parameter doesn't exist (member doesn't exist)
    old = getattr(getParameters(), name)

    # Ensure the given value is an alright type
    if not isinstance(value, type(value)):
        raise TypeError(f"To set {name} of parameters, it must be of the same type as {old} (current value)")

    setattr(getParameters(), name, value)


def makeFileButtonText(selectedFile):
    return f"Select Slit Mask ({selectedFile})"


class ParametersPanel(WindowPanel):
    def showFileSelector(self):
        self.fileBrowser.enabled = True
        self.fileBrowser.visible = True
        self.enabled = False  # Hide parameters panel
        self.visible = False

    def onSelectFile(self, paths):
        path: Path = paths[0]
        setParam("occluder", Image.open(path))  # Set parameter to selected image
        self.fileButton.text = makeFileButtonText(path.name)
        self.enabled = True  # Show parameters panel
        self.visible = True

    #
    def onSelectFileCancelled(self):
        self.enabled = True  # Show parameters panel
        self.visible = True
        self.fileBrowser.visible = False
        self.fileBrowser.enabled = False

    def updateResolution(self, slider: Slider) -> float:
        """Sets the value on the slider to an appropriate resolution. Returns the new value"""
        slider.value = utils.find_nearest_2n(slider.value)
        return slider.value

    def updateLowResolution(self):
        setParam("lowResolution", self.updateResolution(self.lowResolution))

    def updateHighResolution(self):
        setParam("highResolution", self.updateResolution(self.highResolution))

    def clickSimulate(self):
        getParameters().printToConsole()
        self.simulateFunction()

    def __init__(self, simulateFunction: Callable):
        """
        simulateFunction: function that will be called when the simulate button is called
        """

        self.simulateFunction = simulateFunction

        # UI elements:

        self.wavelength = ThinSlider(min=200, max=1000, default=500)
        self.wavelength.on_value_changed = lambda: setParam("wavelength", self.wavelength.value)

        self.brightness = ThinSlider(min=1, max=1000, step=1)
        self.brightness.on_value_changed = lambda: setParam("brightnessFactor", self.brightness.value)

        self.tick = ThinSlider(min=100, max=800, default=300)
        self.tick.on_value_changed = lambda: setParam("tick_distance", self.tick.value)

        self.fileButton = Button(makeFileButtonText(None))
        self.fileBrowser = FileBrowser(
            file_types=[".jpeg", ".jpg", ".png"],
            start_path=Path("images").resolve(),
            visible=False,  # This only shows when it is opened with the fileButton
            enable=False
        )
        # Open the file selector
        self.fileButton.on_click = self.showFileSelector
        # The submit button on the file selector
        self.fileBrowser.on_submit = self.onSelectFile
        # The close button and the little x at the corner of the file selector
        self.fileBrowser.cancel_button.on_click = self.onSelectFileCancelled
        self.fileBrowser.cancel_button_2.on_click = self.onSelectFileCancelled

        self.visualizerAmount = ThinSlider(min=2, max=10, default=2, step=1)
        self.visualizerAmount.on_value_changed = lambda: setParam("visualizerAmount", self.visualizerAmount.value)

        self.detectorDistance = ThinSlider(min=10, max=1000, default=500)
        self.detectorDistance.on_value_changed = lambda: setParam("detectorDistance", self.detectorDistance.value)

        self.lowResolution = ThinSlider(min=16, max=128, step=16, default=16)
        self.lowResolution.on_value_changed = lambda: self.updateLowResolution()

        self.highResolution = ThinSlider(min=32, max=516, step=32, default=32)
        self.highResolution.on_value_changed = lambda: self.updateHighResolution()

        self.simulate = Button(text="Run Simulation")
        self.simulate.on_click = lambda: getParameters().printToConsole()

        super().__init__(title="Simulation Parameters", position=(-.5, .25), content=(
            Text("Wavelength"),
            self.wavelength,
            Text("Tick Distance"),
            self.tick,
            Text("Brightness Factor"),
            self.brightness,
            self.fileButton,
            Text("Number of visualizers"),
            self.visualizerAmount,
            Text("Distance to last visualizer"),
            self.detectorDistance,
            Text("Low Resolution"),
            self.lowResolution,
            Text("High Resolution (Last visualizer)"),
            self.highResolution,
            self.simulate
        ))
