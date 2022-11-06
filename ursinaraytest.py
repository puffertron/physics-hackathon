from ursina import *
from PIL import Image
import struct
import utils

app = Ursina()

resolution = 16

uvtex = Texture(Image.new(mode="RGBA", size=(resolution,resolution), color=(255,0,0,255)))
uvtex.default_filtering = None


occtex = Image.open('images/2slit.png')
# occtex = occtex.resize((resolution, resolution), resample=0)
occtex = Texture(utils.resize_image(occtex, 16, 16))



occulder = Entity(model='plane', texture=occtex, position=Vec3(0,2,0))


subdetector = Entity(model='plane', position=(0,1,0))

detector = Entity(model='plane', texture=uvtex) # set a PIL texture

uv = Entity(model='plane', texture=uvtex) # set a PIL texture



#UVMAP
for x in range (0, uv.texture.width):
    for y in range (0, uv.texture.height):
        uv.texture.set_pixel(x, y, rgb(x*255/resolution, y*255/resolution,0))

uv.texture.apply()


ed = EditorCamera()
ed.enabled=True

app.run()