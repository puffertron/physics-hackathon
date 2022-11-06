import struct
from parameters import Parameters
from ursina import *
from dataclasses import dataclass
from typing import List
import calculations


@dataclass
class Contribution:
    dist: float
    vec: Vec2

class VisualizerPixel:
    def __init__(self, param:Parameters, coordinates:Vec2, distz:float, highRes:bool):
        self.coordinates:Vec2 = coordinates
        self.contributions:List[Contribution] = []
        self.total_contribution:Vec2 = Vec2(0,0)
        
        if highRes:
            holes = param.occluder
        else:
            holes = []#TODO - kidaneFunction(param.occluder,param.lowResolution)
            
        for hole in holes: #TODO make it use the proper occluder from the instance of parameters
            distance = calculations.distance(coordinates.x,coordinates.y,distz)
            individualContribution:Contribution = Contribution(distance,Vec2(calculations.cartesian(distz,distance,param.wavelength)))
            self.contributions.append(individualContribution)
    
class Visualizer:
    def __init__(self, param:Parameters, distz:float, resolution:int, highRes:bool):
        self.distz:float = distz
        self.pixels:List[VisualizerPixel] = []
        
        for x in range(resolution):
            for y in range(resolution):
                self.pixels.append(VisualizerPixel(param, Vec2(x,y), distz, highRes))
        

def setUpTimeState(param:Parameters) -> List[Visualizer]:
    visualizers:List[Visualizer] = []
    for i in range(param.visualizerAmount):
        visualizers.append(Visualizer(param,param.detectorDistance/param.visualizerAmount * i, param.lowResolution, False)) #TODO replace resoliution with lowresolution
    return visualizers
    
    #param.detectorDistance/param.visualizerAmount * self.index

def setUpFinalDetectorState(param:Parameters) -> Visualizer:
    return Visualizer(param, param.detectorDistance, param.highResolution, True)