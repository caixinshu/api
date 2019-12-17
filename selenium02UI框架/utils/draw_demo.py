#!/usr/bin/env python
# -*- coding=utf-8 -*-

from PIL import Image,ImageFilter,ImageOps
import os

def Formula(x,y,alpha):

    return min(int(x*255/(256-y*alpha)),255)

def SketchDrawer(image,blur=6,alpha=1.0):
    image_name = os.path.splitext(image)[0]

    image = Image.open(image)

    luminance_image = image.convert('L')
    luminance_img_copy = luminance_image.copy()
    inverted_image = ImageOps.invert(luminance_img_copy)
    for i in range(blur):
        inverted_image = inverted_image.filter(ImageFilter.BLUR)

    width,height = luminance_image.size

    for x in range(width):
        for y in range(height):
            pixel_luminance = luminance_image.getpixel((x,y))
            pixel_inverted = inverted_image.getpixel((x,y))
            luminance_image.putpixel((x,y),Formula(pixel_luminance,pixel_inverted,alpha))

    luminance_image.show()
    luminance_image.save('{0}_L.jpg'.format(image_name))

if __name__ == '__main__':

    SketchDrawer('5d0fbe57e2efde3b069fd50c.jpg')













