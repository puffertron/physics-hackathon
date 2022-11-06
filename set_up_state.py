import struct
from parameters import Parameters
import parameters
import utils
from ursina import *
from dataclasses import dataclass
from typing import List, Dict, Tuple
import calculations
import pickle
import math
import multiprocessing.dummy as mp
from itertools import product, repeat


@dataclass
class Contribution:
    dist: float
    vec: Vec2

# class VisualizerPixel:  #THREADED
#     def thread_holes(self, hole, coordinates, distz):
#         distance = calculations.distance(coordinates.x-hole.x,coordinates.y-hole.y,distz)
#         individualContribution:Contribution = Contribution(distance,Vec2(calculations.cartesian(distz,distance,parameters.Instance.wavelength)))
#         self.contributions.append(individualContribution)

#     def __init__(self, param:Parameters, coordinates:Vec2, distz:float, holes:List[Vec2]):
#         self.coordinates:Vec2 = coordinates
#         self.contributions:List[Contribution] = []
#         self.totalContribution:Vec2 = Vec2(0,0)
        
#         p=mp.Pool(2)
#         p.starmap(self.thread_holes, zip(holes, repeat(coordinates), repeat(distz)))
#         p.close()
#         p.join()

#         # for hole in holes:
#         #     distance = calculations.distance(coordinates.x-hole.x,coordinates.y-hole.y,distz)
#         #     individualContribution:Contribution = Contribution(distance,Vec2(calculations.cartesian(distz,distance,param.wavelength)))
#         #     self.contributions.append(individualContribution)

class VisualizerPixel:
    def __init__(self, param:Parameters, coordinates:Vec2, distz:float, holes:List[Vec2]):
        self.coordinates:Vec2 = coordinates
        self.contributions:List[Contribution] = []
        self.totalContribution:Vec2 = Vec2(0,0)     

        for hole in holes:
            distance = calculations.distance(coordinates.x-hole.x,coordinates.y-hole.y,distz)
            individualContribution:Contribution = Contribution(distance,Vec2(calculations.cartesian(distz,distance,param.wavelength)))
            self.contributions.append(individualContribution)
    
# class Visualizer: #THREADS!!!!
#     def thread_pixels(self, x, holes, resolution, distz):
#         print(f"Starting row {x} for Visualizer at dist {distz}")
#         for y in range(resolution):
#             self.pixels.append(VisualizerPixel(parameters.Instance, Vec2(x,y), distz, holes)) 

#     def __init__(self, param:Parameters, distz:float, resolution:int, holes:List[Vec2]):
#         self.distz:float = distz
#         self.pixels:List[VisualizerPixel] = []

#         p=mp.Pool(4)
#         p.starmap_async(self.thread_pixels, zip(range(0,resolution), repeat(holes), repeat(resolution), repeat(distz)))
#         p.close()
#         p.join()
        

class Visualizer:
    def __init__(self, param:Parameters, distz:float, resolution:int, holes:List[Vec2]):
        self.distz:float = distz
        self.pixels:List[VisualizerPixel] = []
        
        for x in range(resolution):
            print(f"Starting row {x} for Visualizer at dist {distz}")
            for y in range(resolution):
                self.pixels.append(VisualizerPixel(param, Vec2(x,y), distz, holes))
        

def setUpTimeState(param:Parameters, cache=0, usecache=0) -> List[Visualizer]:
    visualizers:List[Visualizer] = []
    if usecache == 0: #if no use cache
        print("start:")
        c = time.perf_counter()

        lowResHoles:List[Vec2] = utils.get_occlusion_holes(Texture(utils.resize_image(param.occluder,param.lowResolution))) #Uses low res occluder
        print(lowResHoles)
        for i in range(param.visualizerAmount):
            visualizers.append(Visualizer(param,param.detectorDistance/param.visualizerAmount * (i+1), param.lowResolution, lowResHoles))


        print(f"elapsed: {time.perf_counter()-c}")

        if cache == 1:
            #cache if needed
            f = open("cache.pkl", "wb")
            cache = pickle.dump(visualizers, f)
            print("cache written")
            f.close()

    else: #if yee cache
        #check for cache
        file = None
        try:
            file = open("cache.pkl", "rb")
        except:
            #cache is not there:
            print("cache does not exist")
            visualizers = setUpTimeState(param, cache=cache, usecache=0)
        else:
            visualizers = (pickle.load(file))
            file.close()
            print("cache got")

    return visualizers

    
#Ciaran's added code to sort the values by d-step so that the actual simulation part can run faster, will take longer to set up though    
def modifiedSetUpTimeState(param:Parameters) -> Tuple[List[List[Dict[Vec2,Vec2]]], List[Visualizer]]:
    '''returns a list where where each element represents one visualizer with a list of time steps, each time step is a dictionary where the keys are the coordinates to a point on the visualizer and the values are the contribution vectors to be added in that step. The second thing is the original big data structure'''
    maxNumberOfSteps:int = math.ceil(calculations.distance(param.lowResolution, param.lowResolution, param.detectorDistance) / param.tick_distance) #Max distance / distance per tick, rounded up
    planesToAddOverTime:List[List[Dict[Vec2,Vec2]]] = []*param.visualizerAmount # We have one big list for each visualizer
    
    visualizers:List[Visualizer] = setUpTimeState(param)
    for visualizer in visualizers:
        visualizerContributionPlane:List[Dict[Vec2,Vec2]] = []*maxNumberOfSteps #Each dict has space for a whole plane of points, and we have a dictionary for every step 
        for pixel in visualizer.pixels:
            for contribution in pixel.contributions:
                properTimeStep:int = math.ceil(contribution.dist / param.tick_distance) #Distance / distance per tick, rounded up
                #the contribution should be added to the plane corresponding to the above time step
                if (visualizerContributionPlane[properTimeStep-1]).get[pixel.coordinates] == None:
                    (visualizerContributionPlane[properTimeStep-1])[pixel.coordinates] = contribution.vec
                else:
                    (visualizerContributionPlane[properTimeStep-1])[pixel.coordinates] += contribution.vec
                """
                (planesToAddOverTime[properTimeStep-1]) - acesses an element in the list which is a dictionary - darn zero indexing making it confusing
                [pixel.coordinates] - access that dictionary at key of vector being the coordinates
                
                 = contribution.vec - sets the value at this key to the contribution if it isn't defined yet
                 += contribution.vec - adds the value to the key if the value is already defined
                """
        planesToAddOverTime.append(visualizerContributionPlane)
    
    return planesToAddOverTime, visualizers

def setUpFinalDetectorState(param:Parameters) -> Visualizer:
    return Visualizer(param, param.detectorDistance, param.highResolution, utils.get_occlusion_holes(Texture(param.occluder))) #Uses High Res Holes