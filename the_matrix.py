#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 07:11:41 2018

@author: Rorschach
@mail: 188581221@qq.com
"""
import warnings
warnings.filterwarnings('ignore')


import numpy as np  
np.set_printoptions(threshold=np.inf) 
from PIL import Image, ImageDraw, ImageFont

def create_captcha(text, shear=0, size=(17,15)):
    im = Image.new('L', size, 'black')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(r'Coval-Black.otf', 17)
    draw.text((0, -4), text, fill=1, font=font)
    image = np.array(im, dtype='int')
    return image  #归一化处理

m = create_captcha('M')
a = create_captcha('A')
t = create_captcha('T')
r = create_captcha('R')
i = create_captcha('I')
x = create_captcha('X')

go = [m,a,t,r,i,x]
for z in go:
    print(z, end=' ')
    print(' ')







