#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:47:33 2019

@author: hongyisu
"""
#purpose: put pic2 replace part of pic1 
import cv2
img_pic1 = cv2.imread('pic1.jpg')
img_pic2 = cv2.imread('pic2.jpg')

wide_pic1, height_pic1 = img_pic1.shape[:2]
wide_pic2, height_pic2 = img_pic2.shape[:2]

scale = wide_pic1 / wide_pic2 / 4

img_pic2 = cv2.resize(img_pic2, (0,0), fx=scale,fy=scale)
wide_pic2, height_pic2 = img_pic2.shape[:2]

for c in range(0,3):
    img_pic1[wide_pic1 - wide_pic2:, height_pic1 - height_pic2:,c] =img_pic2[:,:,c]

cv2.imwrite('new_pic1.jpg',img_pic1)
