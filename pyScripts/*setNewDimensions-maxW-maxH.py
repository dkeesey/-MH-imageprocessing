# create a python script that will set the new dimensions of the images, and takes two arguments: maxW and maxH
# then resizes images to the maximum width, but if the resulting height exceeds the max height, then resize to the
# maximum height instead.
# example: python setNewDimensions-maxW-maxH.py 200 100
# this will resize all images to a maximum width of 200px, but if the resulting height exceeds 100px, then resize to
# a maximum height of 100px instead.

import os
import sys
from PIL import Image

# get the arguments
maxW = int(sys.argv[1])
maxH = int(sys.argv[2])

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

        # check if the width is greater than the height
        if w > h:
            # check if the width is greater than the maximum width
            if w > maxW:
                # resize the image to the maximum width
                img = img.resize((maxW, int(maxW * h / w)), Image.ANTIALIAS)
        else:
            # check if the height is greater than the maximum height
            if h > maxH:
                # resize the image to the maximum height
                img = img.resize((int(maxH * w / h), maxH), Image.ANTIALIAS)

        # save the image
        img.save(file)

        # give status message that says the filename has been resized to the width and height
        print(file + ' has been resized to ' +
              str(img.size[0]) + 'x' + str(img.size[1]))

        # close the image
        img.close()

# exit the program
sys.exit()
