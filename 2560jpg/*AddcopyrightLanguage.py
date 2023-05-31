from PIL import Image, ImageDraw, ImageFont
import os
import sys


# Set the directory to the current directory
directory = os.getcwd()

# Set the input and output directories
input_directory = "./"
output_directory = "./output"

# Set the text and metadata values
text_content = "©2023 Masumi Hayashi Foundation"
# Replace with the actual path to the Montserrat font file
font_path = "../fonts/Montserrat-SemiBold.ttf"

# Get a list of TIFF files in the input directory
file_list = [file for file in os.listdir(
    input_directory) if file.endswith(".jpg")]

# Get the font size from command line arguments
font_size = int(sys.argv[1]) if len(sys.argv) > 1 else 24

# Loop through each TIFF file
for file_name in file_list:
    # Open the TIFF image
    image_path = os.path.join(input_directory, file_name)
    image = Image.open(image_path)

    # Get the width and height of the image
    width, height = image.size

    # Create a draw object and font object
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the position of the text (bottom left corner of the image)
    text_position = (10, height - font_size)

    # Add the text to the image
    draw.text(text_position, text_content, fill="white", font=font)

    # Generate the new file name
    new_file_name = os.path.splitext(file_name)[0] + "_watermarked.jpg"

    # Save the image
    output_path = os.path.join(output_directory, new_file_name)
    image.save(output_path)

    # Close the image
    image.close()

print("Image processing completed.")
