from ursina import *
from parameters_panel import ParametersPanel
import parameters
import t_sim

app = Ursina(title="Wave Simulation")



if __name__ == "__main__":

    parameters.initParams()
    paramPanel = ParametersPanel()

    

    running:bool = True

    sim = t_sim.Simulation()
    sim.begin() #get the visualiserss

    
    #def update(): #This is our main loop that runs FOREVEEEERRRRR (or until running is False, but that never really happens, our code is eternal and shall never die)
        #currentTickDistance += parameters.Instance.tick_distance
        #sim.update(v, currentTickDistance)
        #print(f"update frame: {currentTickDistance}")
    app.run()

