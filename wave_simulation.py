from ursina import *

from parameters_panel import ParametersPanel
import parameters
from t_sim import Simulation
import t_sim_threading

app = Ursina(title="Wave Simulation")
sim: Simulation = None


def simulate():
    global sim

    print("SoftInstance:")
    parameters.SoftInstance.printToConsole()

    parameters.Instance = deepcopy(parameters.SoftInstance)

    print("Instance")
    parameters.Instance.printToConsole()

    sim = Simulation()
    # sim = t_sim_threading.Simulation() DOES NOT WORK
    sim.begin()


def stop_simulation():
    sim.disable()  # TODO: seems to do nothing if the sim is running
    destroy(sim)
    pass


if __name__ == "__main__":
    parameters.initParams()
    paramPanel = ParametersPanel(simulate, stop_simulation)

    cam = camera
    cam.position = Vec3(7, 7, -7)
    cam.look_at(Vec3(0, 0, 0), 'forward')
    cam.rotation_z = 0

    app.run()
