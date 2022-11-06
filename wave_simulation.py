import dataclasses

from ursina import *
from parameters import Parameters

app = Ursina(title="Wave Simulation")
ed = EditorCamera

__softParameters: Parameters = Parameters()
parameters: Parameters = __softParameters


def simulate():
    global parameters
    parameters = dataclasses.replace(__softParameters)


if __name__ == "__main__":
    simulateButton = Button("Start Simulation")
    simulateButton.on_click = simulate



    app.run()

