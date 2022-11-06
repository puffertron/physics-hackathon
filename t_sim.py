from ursina import *
from PIL import Image
import utils 
import parameters
from typing import List
from set_up_state import Visualizer

def init_planes():
    pass

def render_occluder(tex):
    occluder = Entity(mplanesodel='plane', texture=tex, position=Vec3(0,3,0))

def render_visualisers(visuals):
    for i, v in enumerate(visuals, start=1):
        #TODO: Vary alpha/hue per plane
        tex = Texture(Image.new(mode="RGBA", size=(parameters.Instance.lowResolution, parameters.Instance.lowResolution), color=(255,0,0,255)))
        plane = Entity(model='plane', texture=tex, position=(0,i,0))


def update():
    pass

app = Ursina(title="Wave Simulation")
ed = EditorCamera

#get initialised planes
visualisers = set_up_state.setUpTimeState(params)

#render occluder
render_occulder(occtex)
render_visualisers(visualisers)






#Logic for this code once it's cleaned up

#update every pixel of every visualizer to add any waves that have reached it
def update(timeState:List[Visualizer], currentTickDistance:int):
    for visualizer in timeState:
        for visualizerPixel in visualizer.pixels:
            for contribution in visualizerPixel.contributions:
                if (currentTickDistance-parameters.Instance.tick_distance) < contribution.dist and contribution.dist <= currentTickDistance:
                    visualizerPixel.totalContribution += contribution.vec
                    
    #Then just need to draw it on the screen now that the pixel values are updated


#