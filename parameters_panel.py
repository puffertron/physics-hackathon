from ursina import *
from ursina.prefabs.file_browser import FileBrowser
import parameters


def getParameters():
    return parameters.SoftInstance


class WavelengthSelector(Slider):

    def on_value_changed(self):
        print("Updated wavelength")
        getParameters().printToConsole()
        getParameters().wavelength = self.value

    def __init__(self):
        super(WavelengthSelector, self).__init__()


class BrightnessSelector(Slider):

    def on_value_changed(self):
        getParameters().brightness = self.value


class TickSelector(Slider):

    def on_value_changed(self):
        pass


class OccluderSelector(FileBrowser):

    def on_value_changed(self):
        pass


class VisualizerSelector(Slider):

    def on_value_changed(self):
        pass


class DetectorDistanceSelector(Slider):

    def on_value_changed(self):
        pass


class LowResSelector(Slider):

    def on_value_changed(self):
        pass


class HighResSelector(Slider):

    def on_value_changed(self):
        pass


class ParametersPanel(WindowPanel):

    debug = None

    def __init__(self):

        self.debug = Button("Debug")
        self.debug.on_click = lambda: getParameters().printToConsole()

        super().__init__(title="Simulation Parameters", content=(
            Text("Wavelength"),
            WavelengthSelector(),
            Text("Brightness Factor"),
            BrightnessSelector(),
            self.debug
        ))
