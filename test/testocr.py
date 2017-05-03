#!/usr/bin/python
# coding:utf8

import pytesseract
from PIL import Image
'''
image1 = Image.open('/home/fly/Desktop/phototest.tif')
vcode1 = pytesseract.image_to_string(image1)
print vcode1
'''
print

image2 = Image.open('/home/fly/Desktop/Code')
vcode2 = pytesseract.image_to_string(image2)
print vcode2