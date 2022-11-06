from ursina import *
from parameters_panel import ParametersPanel
import parameters

app = Ursina(title="Wave Simulation")
ed = EditorCamera


if __name__ == "__main__":

    paramPanel = ParametersPanel()



    running:bool = True
    currentTickDistance:float = 0
    while running: #This is our main loop that runs FOREVEEEERRRRR (or until running is False, but that never really happens, our code is eternal and shall never die)
        currentTickDistance += parameters.Instance.tick_distance
    app.run()

