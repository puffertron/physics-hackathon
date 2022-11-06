from ursina import *
from ursina.prefabs.file_browser import FileBrowser
import parameters


def getParameters():
    return parameters.softInstance


class WavelengthSelector(Slider):

    def on_value_change(self):
        getParameters().wavelength = self.value


class BrightnessSelector(Slider):

    def on_value_change(self):
        getParameters().brightness = self.value


class TickSelector(Slider):

    def on_value_change(self):
        pass


class OccluderSelector(FileBrowser):

    def on_value_change(self):
        pass


class VisualizerSelector(Slider):

    def on_value_change(self):
        pass


class DetectorDistanceSelector(Slider):

    def on_value_change(self):
        pass


class LowResSelector(Slider):

    def on_value_change(self):
        pass


class HighResSelector(Slider):

    def on_value_change(self):
        pass


class ParametersPanel(WindowPanel):

    def __init__(self):
        super(ParametersPanel, self).__init__()

        self.content.append(Text("Wavelength"))








