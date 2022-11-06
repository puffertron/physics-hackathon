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


class Simulation(Entity):
    def __init__(self):
        super().__init__()
        self.currenttickdistance = 0
        self.zoffset = 2
        self.visualisers = []

    def create_occluder(self,tex):
        #occluder params texture is an IMAGE instance not TEXTURE
        occluder = Entity(model='plane', texture=Texture(tex), position=Vec3(0,self.zoffset,0))
        return occluder

    def create_visualisers(self, visuals):
        l = []
        for i, v in enumerate(visuals, start=1):
            spacing = 4/len(visuals)

            if i != len(visuals):
                tex = Texture(Image.new(mode="RGBA", size=(parameters.Instance.lowResolution, parameters.Instance.lowResolution), color=(255,0,0,100)))
                plane = Entity(model='plane', texture=tex, position=(0,self.zoffset-i*spacing,0))
            
            else: #special case for final visualiser AKA detector
                tex = Texture(Image.new(mode="RGBA", size=(parameters.Instance.lowResolution, parameters.Instance.lowResolution), color=(0,0,0,255)))
                plane = Entity(model='plane', texture=tex, position=(0,self.zoffset-i*spacing,0))

            l.append(plane)
        return l


    def apply_pixels(visualisers, self):

        pass

    visgroup: List[Entity] = []
    occluder = None



    
    def begin(self):
        #get initialised planes
        visualisers = set_up_state.setUpTimeState(parameters.Instance)
        self.occluder = self.create_occluder(parameters.Instance.occluder)
        self.visgroup += (self.create_visualisers(visualisers))
        
        self.visualisers = visualisers
        print("begun")


    #Logic for this code once it's cleaned up

    #update every pixel of every visualizer to add any waves that have reached it
    def update(self):
        print(f"update frame{self.currenttickdistance}")
        for i, visualizer in enumerate(self.visualisers):
            for visualizerPixel in visualizer.pixels:
                for contribution in visualizerPixel.contributions:
                    if (self.currenttickdistance-parameters.Instance.tick_distance) < contribution.dist and contribution.dist <= self.currenttickdistance:
                        visualizerPixel.totalContribution += contribution.vec
                #color pixels
                v = self.visgroup[i]
                b = int(utils.length(visualizerPixel.totalContribution)*parameters.Instance.brightnessFactor)
                v.texture.set_pixel(int(visualizerPixel.coordinates.x),
                                    int(visualizerPixel.coordinates.y),
                                    rgb(b, b, b))
        
        self.currenttickdistance += 1
                        
        #Then just need to draw it on the screen now that the pixel values are updated


    #
