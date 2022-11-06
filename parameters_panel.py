from typing import Callable
from PIL import Image
from ursina import *
from ursina.prefabs.file_browser import FileBrowser
import parameters
import utils


def get_params():
    return parameters.SoftInstance


def set_param(name: str, value):
    print(f"Setting {name} to {value}")

    # This throws an error if the parameter doesn't exist (member doesn't exist)
    old = getattr(get_params(), name)

    # Ensure the given value is an alright type
    if not isinstance(value, type(value)):
        raise TypeError(f"To set {name} of parameters, it must be of the same type as {old} (current value)")

    setattr(get_params(), name, value)


def make_file_button_text(selectedFile):
    return f"Select Slit Mask ({selectedFile})"


def updateResolution(slider: Slider) -> float:
    """Sets the value on the slider to an appropriate resolution. Returns the new value"""
    slider.value = utils.find_nearest_2n(slider.value)
    return slider.value


class ParametersPanel(WindowPanel):
    def show_file_selector(self):
        self.file_browser.enabled = True
        self.file_browser.visible = True
        self.enabled = False  # Hide parameters panel
        self.visible = False

    def on_select_file(self, paths):
        path: Path = paths[0]
        set_param("occluder", Image.open(path))  # Set parameter to selected image
        self.file_button.text = make_file_button_text(path.name)
        self.enabled = True  # Show parameters panel
        self.visible = True

    #
    def onSelectFileCancelled(self):
        self.enabled = True  # Show parameters panel
        self.visible = True
        self.file_browser.visible = False
        self.file_browser.enabled = False

    def update_low_res(self):
        set_param("lowResolution", updateResolution(self.low_res))

    def update_high_res(self):
        set_param("highResolution", updateResolution(self.high_res))

    def update_sim_state(self):
        value: str = self.start_stop.value
        if value == "start":
            self.start_sim()
        elif value == "stop":
            self.stop_sim()
        else:
            raise AssertionError(f"Start/Stop button group should have value of start or stop, has {value}")

    def __init__(self, start_sim: Callable, stop_sim: Callable):
        """
        simulateFunction: function that will be called when the simulate button is called
        """

        self.start_sim = start_sim
        self.stop_sim = stop_sim

        # UI elements:

        self.wavelength = ThinSlider(min=200, max=1000, default=500)
        self.wavelength.on_value_changed = lambda: set_param("wavelength", self.wavelength.value)

        self.brightness = ThinSlider(min=1, max=1000, step=1)
        self.brightness.on_value_changed = lambda: set_param("brightnessFactor", self.brightness.value)

        self.tick = ThinSlider(min=100, max=800, default=300)
        self.tick.on_value_changed = lambda: set_param("tick_distance", self.tick.value)

        self.file_button = Button(make_file_button_text(None))
        self.file_browser = FileBrowser(
            file_types=[".jpeg", ".jpg", ".png"],
            start_path=Path("images").resolve(),
            visible=False,  # This only shows when it is opened with the fileButton
            enable=False
        )
        # Open the file selector
        self.file_button.on_click = self.show_file_selector
        # The submit button on the file selector
        self.file_browser.on_submit = self.on_select_file
        # The close button and the little x at the corner of the file selector
        self.file_browser.cancel_button.on_click = self.onSelectFileCancelled
        self.file_browser.cancel_button_2.on_click = self.onSelectFileCancelled

        self.visualizer_amount = ThinSlider(min=2, max=10, default=2, step=1)
        self.visualizer_amount.on_value_changed = lambda: set_param("visualizerAmount", self.visualizer_amount.value)

        self.detector_distance = ThinSlider(min=10, max=1000, default=500)
        self.detector_distance.on_value_changed = lambda: set_param("detectorDistance", self.detector_distance.value)

        self.low_res = ThinSlider(min=16, max=128, step=16, default=16)
        self.low_res.on_value_changed = self.update_low_res

        self.high_res = ThinSlider(min=32, max=516, step=32, default=32)
        self.high_res.on_value_changed = self.update_high_res

        self.start_stop = ButtonGroup(("start", "stop"), default="stop")
        self.start_stop.on_value_changed = self.update_sim_state

        super().__init__(title="Simulation Parameters", position=(-.5, .25), content=(
            Text("Wavelength"),
            self.wavelength,
            Text("Tick distance"),
            self.tick,
            Text("Brightness factor"),
            self.brightness,
            self.file_button,
            Text("Number of visualizers"),
            self.visualizer_amount,
            Text("Distance to last visualizer"),
            self.detector_distance,
            Text("Low resolution"),
            self.low_res,
            Text("High resolution (Last visualizer)"),
            self.high_res,
            self.start_stop
        ))
