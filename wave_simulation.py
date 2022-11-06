import dataclasses

from ursina import *
from parameters import Parameters

def doNothing(): pass

app = Ursina(title="Wave Simulation")
ed = EditorCamera

__softParameters: Parameters = Parameters()
parameters: Parameters = __softParameters


def simulate():
    global parameters
    parameters = dataclasses.replace(__softParameters)


if __name__ == "__main__":

    paramPanel = WindowPanel(model=Plane, scale=(0.5, 1, 0), position=(-.8, 0.5, 0), color=color.white)
    paramPanel.on_mouse_exit = doNothing
    paramPanel.on_mouse_enter = doNothing

    simulateButton = Button("Start Simulation", parent=paramPanel, scale=0.1)
    simulateButton.on_click = simulate

    paramPanel.content.append(simulateButton)

    app.run()

