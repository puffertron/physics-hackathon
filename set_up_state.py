import struct
from parameters import Parameters
import utils
from ursina import *
from dataclasses import dataclass
from typing import List
import calculations


@dataclass
class Contribution:
    dist: float
    vec: Vec2

class VisualizerPixel:
    def __init__(self, param:Parameters, coordinates:Vec2, distz:float, holes:List[Vec2]):
        self.coordinates:Vec2 = coordinates
        self.contributions:List[Contribution] = []
        self.totalContribution:Vec2 = Vec2(0,0)
            
        for hole in holes:
            distance = calculations.distance(coordinates.x,coordinates.y,distz)
            individualContribution:Contribution = Contribution(distance,Vec2(calculations.cartesian(distz,distance,param.wavelength)))
            self.contributions.append(individualContribution)
    
class Visualizer:
    def __init__(self, param:Parameters, distz:float, resolution:int, holes:List[Vec2]):
        self.distz:float = distz
        self.pixels:List[VisualizerPixel] = []
        
        for x in range(resolution):
            for y in range(resolution):
                self.pixels.append(VisualizerPixel(param, Vec2(x,y), distz, holes))
        

def setUpTimeState(param:Parameters) -> List[Visualizer]:
    visualizers:List[Visualizer] = []
    for i in range(param.visualizerAmount):
        visualizers.append(Visualizer(param,param.detectorDistance/param.visualizerAmount * (i+1), param.lowResolution, utils.get_occlusion_holes(Texture(utils.resize_image(param.occluder,param.lowResolution))))) #Uses low resolution occluder
    return visualizers
    

def setUpFinalDetectorState(param:Parameters) -> Visualizer:
    return Visualizer(param, param.detectorDistance, param.highResolution, utils.get_occlusion_holes(Texture(param.occluder))) #Uses High Res Holes