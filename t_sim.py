from ursina import *
from PIL import Image
import utils 
import parameters
import set_up_state
from typing import List, Dict
from set_up_state import Visualizer

##some settings


class Simulation(Entity):
    def __init__(self):
        super().__init__()
        self.currentTick = 0
        self.currentTickDistance = 0
        self.zoffset = 2
        self.visualisers = []

    def create_occluder(self,tex):
        #occluder params texture is an IMAGE instance not TEXTURE
        occluder = Entity(model='plane', texture=Texture(tex), position=Vec3(0,self.zoffset,0))
        return occluder

    def create_visualisers(self, visuals):
        l = []
        for i, v in enumerate(visuals, start=1):
            spacing = 4/len(visuals) #TODO - The length is distorted from the value in parameters - not sure what a good fix is

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
        #self.visualisers = set_up_state.setUpTimeState(parameters.Instance, cache=1, usecache=0)
        #self.occluder = self.create_occluder(parameters.Instance.occluder)
        #self.visgroup += (self.create_visualisers(self.visualisers))

        #DEBUG UV SQUARE
        #res = parameters.Instance.lowResolution
        #uvtex = Texture(Image.new(mode="RGBA", size=(res,res), color=(255,0,0,255)))
        #uvtex.default_filtering = None
        #uv = Entity(model='plane', texture=uvtex, position=(0,-3,0)) # set a PIL texture
        #for x in range (0, uv.texture.width):
        #    for y in range (0, uv.texture.height):
        #        uv.texture.set_pixel(x, y, rgb(x*255/res, y*255/res,0))

        #uv.texture.apply()

        
        #From old slower way
        #self.visualisers = set_up_state.setUpTimeState(parameters.Instance)
        
        #For newer faster way
        self.tempTuple = set_up_state.modifiedSetUpTimeState(parameters.Instance)
        self.planesToAddOverTime:List[List[Dict[Vec2,Vec2]]] = self.tempTuple[0]
        self.visualisers:List[Visualizer] = self.tempTuple[1]
        self.lastTick = self.tempTuple[2]
        
        self.occluder = self.create_occluder(parameters.Instance.occluder)
        self.visgroup += (self.create_visualisers(self.visualisers))
        
        print("begun")


    #Logic for this code once it's cleaned up

    #update every pixel of every visualizer to add any waves that have reached it
    def update(self):
        if math.ceil(self.currentTickDistance / parameters.Instance.tick_distance) <= self.lastTick:
            #t = time.perf_counter()
            print(f"update frame {self.currentTick} of {self.lastTick}")
            for i, visualizer in enumerate(self.visualisers):
                currentVisualizerPlaneToAdd = self.planesToAddOverTime[i] #Putting this here so it doesn't have to do an extra accessing element on a list every time
                for visualizerPixel in visualizer.pixels:
                    
                    #Old slower code from older set up function
                    #for contribution in visualizerPixel.contributions:
                    #    if (self.currentTickDistance-parameters.Instance.tick_distance) < contribution.dist and contribution.dist <= self.currenttickdistance:
                    #        visualizerPixel.totalContribution += contribution.vec
                    
                    #Newer faster code for modified set up function
                    if (currentVisualizerPlaneToAdd[math.ceil(self.currentTickDistance / parameters.Instance.tick_distance) - 1] is not None) and (visualizerPixel.coordinates in self.planesToAddOverTime[i][math.ceil(self.currentTickDistance / parameters.Instance.tick_distance) - 1]): #TODO stop redoing calc over and over again
                        visualizerPixel.totalContribution += self.planesToAddOverTime[i][math.ceil(self.currentTickDistance / parameters.Instance.tick_distance) - 1][visualizerPixel.coordinates]
                    '''
                    [i] - acesses the visualizer
                    [math.ceil(self.currenttickdistance / parameters.Instance.tick_distance)] - acesses the dictionary for the given distance step
                    [visualizerPixel.coordinates] - acesses the key that is the position vector of the pixel on the visualizer (the value is the contribution to add for that frame)
                    '''
                    
                    #color pixels
                    v = self.visgroup[i]
                    b = min(int(utils.length(visualizerPixel.totalContribution)*parameters.Instance.brightnessFactor), 255)
                    v.texture.set_pixel(int(visualizerPixel.coordinates.x),
                                        int(visualizerPixel.coordinates.y), rgb(b, b, b))
                    v.texture.apply()
                    #print(f"{visualizerPixel.coordinates.x} - {visualizerPixel.coordinates.y}")
            
            self.currentTick += 1
            self.currentTickDistance += parameters.Instance.tick_distance
            #print(time.perf_counter()-t)
                        
        #Then just need to draw it on the screen now that the pixel values are updated


    #
