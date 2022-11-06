from parameters import Parameters
from set_up_state import setUpFinalDetectorState

def final_State_Simulate(param:Parameters, spaceToDrawOn:type): #Replace spaceToDraw with what it should be
    detectorState = setUpFinalDetectorState(param)
    
    #Add C to C_total for every hole, so after this all of total_contribution's should be total values
    for detectorPixel in detectorState.pixels:
        for holeContribution in detectorPixel.contributions:
            detectorPixel.total_contribution += holeContribution.vec
        
    