from ursina import *
import parameters
from PIL import Image


def resize_image(img: Image, size):
    img = img.resize((size,size), resample=0)
    return img

def length(vec: Vec2):
    l = sqrt(vec.x**2+vec.y**2)
    return l


def get_occlusion_holes(tex: Texture):
    holes = []
    for x in range(0, tex.width):
        for y in range(0, tex.height):
            print (f"pixel{x},{y}: b:{tex.get_pixel(x,y).brightness}")
            if tex.get_pixel(x, y).brightness < 0.5:
                #these pixels are holes
                holes.append(Vec2(x,y))
    
    return holes