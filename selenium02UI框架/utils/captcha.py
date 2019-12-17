#!/usr/bin/env python
# -*- coding=utf-8 -*-

import random
import string

from PIL import Image,ImageDraw,ImageFont

class Captcha(object):
    '''
    绘制图片验证码
    '''
    number = 4
    size = (100,30)
    fontsize = 25
    line_number = 2

    SOURCE = list(string.ascii_letters)
    for index in range(0,10):
        SOURCE.append(index)



    #绘制干扰线
    @classmethod
    def __gene_line(cls,draw,width,height):
        begin = (random.randint(0,width),random.randint(0,height))
        end = (random.randint(0,width),random.randint(0,height))
        draw.line([begin,end],fill=cls.__gene_random_color(),width=2)


    #绘制干扰点
    @classmethod
    def __gene_point(cls,draw,point_chance,width,height):
        chance = min(100,max(0,int(point_chance)))
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0,100)
                if tmp >100 - chance:
                    draw.point((w,h),fill=cls.__gene_random_color())

    #生成随机颜色
    @classmethod
    def __gene_random_color(cls,start=0,end=255):
        random.seed()
        return (random.randint(start,end),random.randint(start,end),random.randint(start,end))

    #生成一个字体
    @classmethod
    def __gene_random_font(cls):
        fonts = [
            # 'Courgette-Regular.ttf',
            # 'LHANDW.TTF',
            # 'Lobster-Regular.txt',
            'verdana.ttf'
        ]
        font = random.choice(fonts)
        return 'utils/'+font


    #随机生成一个字符串
    @classmethod
    def gene_text(cls,number):
        return ''.join(random.sample(cls.SOURCE,number))

    #生成验证码
    @classmethod
    def gene_graph_captcha(cls):
        width,height = cls.size

        image = Image.new('RGBA', (width,height),cls.__gene_random_color(0,100))
        font =  ImageFont.truetype(cls.__gene_random_font())
        draw = ImageDraw.Draw(image)
        text = cls.gene_text(cls.number)
        font_width,font_height = font.getsize(text)
        draw.text(((width-font_width)/2,(height-font_height)/2),text,font=font,fill=cls.__gene_random_color(155,255))
        for x in range(0,cls.line_number):
            cls.__gene_line(draw,width,height)

        cls.__gene_point(draw,10,width,height)
        with open('captcha.png','wb') as f:
            image.save(f)


        return (text,image)


if __name__ == '__main__':
    Captcha.gene_graph_captcha()


