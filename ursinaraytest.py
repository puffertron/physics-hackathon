from ursina import *
from PIL import Image

app = Ursina()

resolution = 16

uvtex = Texture(Image.new(mode="RGBA", size=(resolution,resolution), color=(255,0,0,255)))
uvtex.default_filtering = None

occulder = Entity(model='plane', texture='2slit.png', position=Vec3(0,2,0))

subdetector = Entity(model='plane', position=(0,1,0))

detector = Entity(model='plane', texture=uvtex) # set a PIL texture

uv = Entity(model='plane', texture=uvtex) # set a PIL texture




#UVMAP
for x in range (0, uvtex.width):
    for y in range (0, uvtex.height):
        uvtex.set_pixel(x, y, rgb(x*255/resolution, y*255/resolution,0))

uvtex.apply()

print("tex:")
print(detector.texture)

ed = EditorCamera()

app.run()