from ursina import *

from parameters_panel import ParametersPanel
import parameters
import t_sim, t_sim_threading

app = Ursina(title="Wave Simulation")



if __name__ == "__main__":

    parameters.initParams()
    #paramPanel = ParametersPanel(FUNCTION HERE)

    #ed = EditorCamera()
    #ed.position.y = 5
    # ed.look_at(Vec3(0,0,0))

    cam = camera
    cam.position = Vec3(7,7,-7)
    cam.look_at(Vec3(0,0,0), 'forward')
    cam.rotation_z = 0

    sim = t_sim.Simulation()
    #sim = t_sim_threading.Simulation() DOES NOT WORK
    sim.begin() #get the visualisers

    app.run()

