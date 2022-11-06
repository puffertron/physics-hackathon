from ursina import *
from PIL import Image
import utils 
import parameters
import set_up_state
from typing import List
from set_up_state import Visualizer

####REMOVE LATER
parameters.initParams()

##some settings
zoffset = 2


def create_occluder(tex:Texture):
    #occluder params texture is an IMAGE instance not TEXTURE
    occluder = Entity(model='plane', texture=Texture(tex), position=Vec3(0,zoffset,0))
    return occluder
def create_visualisers(visuals:Visualizer):
    l = []
    for i, v in enumerate(visuals, start=1):
        #TODO: Vary alpha/hue per plane
        spacing = parameters.Instance.detectorDistance/len(visuals)

        if i != len(visuals):
            tex = Texture(Image.new(mode="RGBA", size=(parameters.Instance.lowResolution, parameters.Instance.lowResolution), color=(255,0,0,100)))
            plane = Entity(model='plane', texture=tex, position=(0,zoffset-i*spacing,0))
        
        else: #special case for final visualiser AKA detector
            tex = Texture(Image.new(mode="RGBA", size=(parameters.Instance.lowResolution, parameters.Instance.lowResolution), color=(255,255,0,255)))
            plane = Entity(model='plane', texture=tex, position=(0,zoffset-i*spacing,0))

        l.append(plane)
    return l


app = Ursina(title="Wave Simulation")
ed = EditorCamera()

#get initialised planes
visualisers = set_up_state.setUpTimeState(parameters.Instance)

#render occluder
o = create_occluder(parameters.Instance.occluder)
v = create_visualisers(visualisers)

##DEBUGG
print("DEBUG:")

#app.run()
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
