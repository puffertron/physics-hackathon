from ursina import *
import parameters
from PIL import Image


def resize_image(img: Image, x, y):
    img = img.resize((x,y), resample=0)
    return img


def get_occlusion_holes(tex: Texture):
    holes = []
    for x in range(0, tex.width):
        for y in range(0, tex.height):
            print (tex.get_pixel(x,y).brightness)
            if tex.get_pixel(x, y).brightness < 0.5:
                #these pixels are holes
                holes.append(Vec2(x,y))
    
    return holes