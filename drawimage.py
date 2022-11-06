from ursina import *
from PIL import Image
import parameters

app = Ursina()


class Canvas(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
    
    def update(self):
        res = parameters.lowResolution
        m = mouse.point
        if mouse.left and m:
            x = int(Vec2((Vec2(m.x,m.z)+Vec2(0.5,0.5))).x * res)
            y = int(Vec2((Vec2(m.x,m.z)+Vec2(0.5,0.5))).y * res)
            print((x,y))
            self.texture.set_pixel(x,y, color.black)
        if mouse.right and m:
            x = int(Vec2((Vec2(m.x,m.z)+Vec2(0.5,0.5))).x * res)
            y = int(Vec2((Vec2(m.x,m.z)+Vec2(0.5,0.5))).y * res)
            print((x,y))
            self.texture.set_pixel(x,y, color.white)
        
        self.texture.apply()


# # uvtex = Texture(Image.new(mode="RGBA", size=(resolution,resolution), color=(255,0,0,255)))
canvtex = Texture(Image.new(mode="RGBA", size=(64,64), color=(255,255,255,255)))
# canvas = Entity(model='plane', texture=canvtex)

# uvtex = Texture(Image.new(mode="RGBA", size=(64,64), color=(255,0,0,255)))
# uv = Entity(model='plane', texture=uvtex) # set a PIL texture

c = Canvas(model='plane', texture=canvtex, collider='box')


cam = camera
cam.position = Vec3(0,4,0)
cam.look_at(Vec3(0,0,0), axis='forward')



app.run()