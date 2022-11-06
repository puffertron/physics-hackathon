from parameters import Parameters
from set_up_state import setUpFinalDetectorState


#DEPRECATED - Final State Sim not actually used, we realized this wouldn't be much faster than t-sim with one visualizer
def final_State_Simulate(param:Parameters, spaceToDrawOn:type): #Replace spaceToDraw with what it should be
    detectorState = setUpFinalDetectorState(param)
    
    #Add C to C_total for every hole, so after this all of total_contribution's should be total values
    for detectorPixel in detectorState.pixels:
        for holeContribution in detectorPixel.contributions:
            detectorPixel.totalContribution += holeContribution.vec
            
    #Now just need to draw magnitude of pixels.totalContribution for every detectorState.pixels at pixel.coordinate
    
    
    