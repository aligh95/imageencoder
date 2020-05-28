import math
import random
from PIL import Image
import numpy as np
from itertools import chain


fileBytes = []
im = Image.open('encoded.png') # encoded image file , can be many different formats.
pix = im.load()
print (im.size) # Get the width and height of the image for iterating over
width = im.size[0]
height = im.size[1]
for x_byte in range(width):
    for y_byte in range(height):
        fileBytes.append(list(pix[x_byte,y_byte]))
        
finalBytes = list(chain(*fileBytes))
newFile = open("decoded_file.mp4", "wb")
#convert bytes to binary for save in file
fileByteArray = bytearray(finalBytes)
# write to file
newFile.write(fileByteArray)
