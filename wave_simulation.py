from ursina import *

from parameters import Parameters

app = Ursina(title="Wave Simulation")
ed = EditorCamera

if __name__ == "__main__":
    simulateButton = Button("Start Simulation")

    app.run()

    params = Parameters()

