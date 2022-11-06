from ursina import *
from PIL import Image

from parameters import Parameters
import set_up_stateplanes


def get_occlusiion_holes(tex: Texture):
    holes = []
    for x in range(0, tex.width):
        for y in range(0, tex.height):
            print (tex.get_pixel(x,y).brightness)
            if tex.get_pixel(x, y).brightness < 0.5:
                #these pixels are holes
                holes.append(Vec2(x,y))
    
    return holes

def render_occulder(tex):
    occulder = Entity(mplanesodel='plane', texture=tex, position=Vec3(0,3,0))

def render_visualisers(visuals):
    for i, v in enumerate(visuals, start=1):
        #TODO: Vary alpha/hue per plane
        tex = Texture(Image.new(mode="RGBA", size=(params.lowResolution, params.lowResolution), color=(255,0,0,255)))
        plane = Entity(model='plane', texture=tex, position=(0,i,0))



app = Ursina(title="Wave Simulation")
ed = EditorCamera
planes
__softParameters: Parameters = Parameters()
parameters: Parameters = __softParameters

    #get initialised planes
    visualisers = set_up_state.setUpTimeState(params)

    #render occluder
    render_occulder(occtex)
    render_visualisers(visualisers)






