#!/usr/bin/env python
# -*- coding=utf-8 -*-

from PIL import Image

ascii_char = list("!@#$%^&*oauldbc,./?';-=+_")

def get_char(r,b,g,alpha = 256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    w = int(432/4)
    h = int(136/4)
    im = Image.open('5d0fbe57e2efde3b069fd50c.jpg')
    im = im.resize((w,h),Image.NEAREST)

    txt = ''

    for i in range(h):
        for j in range(w):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    with open('test.txt','w') as f:
        f.write(txt)