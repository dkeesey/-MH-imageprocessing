# create a python script that will add borders to the images, and takes one argument, or four arguments: borderSize, or
# topBorderSize, rightBorderSize, bottomBorderSize, and leftBorderSize
# example: python AddBorders.py 10
# example: python AddBorders.py 10 20 30 40

import os
import sys
from PIL import Image

# get the arguments
if len(sys.argv) == 2:
    borderSize = int(sys.argv[1])
    topBorderSize = borderSize
    rightBorderSize = borderSize
    bottomBorderSize = borderSize
    leftBorderSize = borderSize

if len(sys.argv) == 5:
    topBorderSize = int(sys.argv[1])
    rightBorderSize = int(sys.argv[2])
    bottomBorderSize = int(sys.argv[3])
    leftBorderSize = int(sys.argv[4])

# get the current working directory
cwd = os.getcwd()

# get the list of files in the current working directory
files = os.listdir(cwd)

# loop through the files
for file in files:
    # get the file extension
    ext = os.path.splitext(file)[1]

    # check if the file is an image
    if ext.lower() in ('.jpg', '.jpeg', '.png', '.gif'):
        # open the image
        img = Image.open(file)

        # get the current width and height
        w, h = img.size

        # calculate the new width and height
        newW = w + leftBorderSize + rightBorderSize
        newH = h + topBorderSize + bottomBorderSize

        # create a new image of the new width and height
        newImg = Image.new(img.mode, (newW, newH), (255, 255, 255))

        # paste the original image into the new image
        newImg.paste(img, (leftBorderSize, topBorderSize))

        # save the new image
        newImg.save(file)

        # give status message that says the filename has been resized to the width and height and border size
        # or if there are different border sizes, then give the status message that says the filename has been
        # resized to the width and height and top border size, right border size, bottom border size, and left border
        # size
        if borderSize:
            print(file + ' has been resized to ' +
                  str(newImg.size[0]) + 'x' + str(newImg.size[1]) + ' with a border size of ' + str(borderSize))
        else:
            print(file + ' has been resized to ' +
                  str(newImg.size[0]) + 'x' + str(newImg.size[1]) + ' with a top border size of ' + str(topBorderSize) +
                  ', right border size of ' + str(rightBorderSize) + ', bottom border size of ' + str(bottomBorderSize) +
                  ', and left border size of ' + str(leftBorderSize))

        # close the image
        img.close()
