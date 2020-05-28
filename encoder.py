import math
from PIL import Image

in_file = open("target.mp4", "rb") # opening for [r]eading as [b]inary
data = in_file.read() # read all bytes
in_file.close() # close file handle
colorByte = [] # create byte of color
filelen = len(data) # get lenght of 

imageXY = int(math.sqrt(int(filelen/4))) # image width and height

for dataByte in range(0,len(data),4): # for in bytes
    if(filelen - dataByte > 4):
        colorByte .append ((data[dataByte], data[dataByte+1], data[dataByte+2],data[dataByte+3])) # append bytes to color
    else:# if the last item of bytes array less than 4 handles with this 
        lastList = []
        try:
            lastList.append(data[dataByte])
            lastList.append(data[dataByte+1])
            lastList.append(data[dataByte+2])
            lastList.append(data[dataByte+3])
        except :
            colorByte .append(tuple(lastList) )
            pass


img = Image.new( 'RGBA', (imageXY,imageXY), "black") # Create a new black image
pixels = img.load() # Create the pixel map
index = 0
for i in range(img.size[0]):    # For every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = colorByte[index] # set tupple to pixel
        index = index + 1
        
img.save('encoded.png')  # save images