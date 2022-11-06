from copy import deepcopy

from ursina import Ursina, destroy, Vec3, camera, window

from parameters_panel import ParametersPanel, MainGui
import parameters
from t_sim import Simulation
import t_sim_threading

app = Ursina(title="Wave Simulation")
window.fps_counter.enabled = False
window.cog_button.enabled = False

gui: MainGui = None

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

    # After simulation has stopped, call gui.stet_stopped()


def stop_simulation():
    sim.enable = False  # TODO: seems to do nothing if the sim is running
    destroy(sim)
    pass


if __name__ == "__main__":
    parameters.initParams()
    gui = MainGui(simulate, stop_simulation)

    cam = camera
    cam.position = Vec3(7, 7, -7)
    cam.look_at(Vec3(0, 0, 0), 'forward')
    cam.rotation_z = 0

    app.run()
