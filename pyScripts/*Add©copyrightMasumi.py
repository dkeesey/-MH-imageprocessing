# create a python script that adds © 2023 Masumi Hayashi Foundation to the bottom left corner of the image,
# aligned with the left edge of the photo, not the border
# Use Montserrat-SemiBold.ttf which is in a sibling directory to this script called 'fonts'
# use White, since the border is black
# take one argument which is the font size

# import the necessary libraries
import os
import sys
from PIL import Image, ImageDraw, ImageFont

# get the arguments
fontSize = int(sys.argv[1])

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

        # create a new image of the new width and height
        newImg = Image.new(img.mode, (w, h), (255, 255, 255))

        # paste the original image into the new image
        newImg.paste(img, (0, 0))

        # get a drawing context
        draw = ImageDraw.Draw(newImg)

        # get the font
        font = ImageFont.truetype('../fonts/Montserrat-SemiBold.ttf', fontSize)

        # get the text size
        textSize = draw.textsize('© 2023 Masumi Hayashi Foundation', font=font)

        # draw the text
        draw.text(
            (0, h - textSize[1]), '© 2023 Masumi Hayashi Foundation', fill=(255, 255, 255), font=font)

        # save the new image
        newImg.save(file)

        # give a new status message that says '© 2023 Masumi Hayashi Foundation'
        # has been added to the bottom left corner
        print('© 2023 Masumi Hayashi Foundation has been added to the bottom left corner of ' + file)

        # close the image
        img.close()
