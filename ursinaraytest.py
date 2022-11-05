from ursina import *
from PIL import Image
import struct

app = Ursina()

resolution = 16

uvtex = Texture(Image.new(mode="RGBA", size=(resolution,resolution), color=(255,0,0,255)))
uvtex.default_filtering = None

occtex = Image.open('images/2slit.png')
occtex = occtex.resize((resolution, resolution), resample=0)
occtex = Texture(occtex)


occulder = Entity(model='plane', texture=occtex, position=Vec3(0,2,0))


subdetector = Entity(model='plane', position=(0,1,0))

detector = Entity(model='plane', texture=uvtex) # set a PIL texture

uv = Entity(model='plane', texture=uvtex) # set a PIL texture

def get_holes(tex: Texture):
    holes = []
    for x in range(0, tex.width):
        for y in range(0, tex.height):
            print (tex.get_pixel(x,y).brightness)
            if tex.get_pixel(x, y).brightness < 0.5:
                #these pixels are holes
                holes.append(Vec2(x,y))
    
    return holes

print(get_holes(occulder.texture))


#UVMAP
for x in range (0, uvtex.width):
    for y in range (0, uvtex.height):
        uvtex.set_pixel(x, y, rgb(x*255/resolution, y*255/resolution,0))

uvtex.apply()


ed = EditorCamera()

app.run()