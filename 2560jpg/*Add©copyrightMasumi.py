# import the necessary libraries
import os
import sys
from PIL import Image, ImageDraw, ImageFont

# get the arguments
fontSize = int(sys.argv[1])

# get the current working directory
cwd = os.getcwd()

# get the parent directory
parentDirectory = os.path.dirname(cwd)


# Set the text and metadata values
text_content = "©2023 Masumi Hayashi Foundation"
# Replace with the actual path to the Montserrat font file
font_path = "../fonts/Montserrat-SemiBold.ttf"

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

        # create a new image of the same dimensions
        newImg = Image.new(img.mode, (w, h), (255, 255, 255))

        # get a drawing context
        draw = ImageDraw.Draw(newImg)

        # get the font
        font = ImageFont.truetype(font_path, fontSize)

        # calculate the text position within the image
        text = '© 2023 Masumi Hayashi Foundation'
        # textWidth, textHeight = draw.textsize(text, font=font)
        # # Position it at the bottom left corner, above the border
        # textPosition = (10, h - textHeight - fontSize)

        # Adjust the y-coordinate for proper alignment
        text_position = (left_margin, canvas_height -
                         bottom_margin + fontSize)

        draw.text(text_position, text_content, fill="white", font=font)

        # draw the text
        draw.text(textPosition, text, fill="white", font=font)

        # save the new image
        newImg.save(file)

        # give a status message indicating the text has been added
        print('Copyright information has been added to ' + file)

        # close the image
        img.close()
