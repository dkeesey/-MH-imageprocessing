from PIL import Image, ImageDraw, ImageFont
import os

# Set the input and output directories
input_directory = "./sourceFiles"
output_directory = "./output"

# Set the desired margin values
top_margin = 15
left_margin = 15
right_margin = 15
bottom_margin = 45

# Set the text and metadata values
text_content = "©2023 Masumi Hayashi Foundation"
# Replace with the actual path to the Montserrat font file
font_path = "./fonts/Montserrat-SemiBold.ttf"

# Get a list of TIFF files in the input directory
file_list = [file for file in os.listdir(
    input_directory) if file.endswith(".tif")]

# Loop through each TIFF file
for file_name in file_list:
    # Open the TIFF image
    image_path = os.path.join(input_directory, file_name)
    image = Image.open(image_path)

    # Resize the image
    new_width = 3840
    new_height = int(image.height * (new_width / image.width))
    resized_image = image.resize((new_width, new_height))

    # Create a new canvas with the desired dimensions and black background
    canvas_width = new_width + left_margin + right_margin
    canvas_height = new_height + top_margin + bottom_margin
    canvas = Image.new("RGB", (canvas_width, canvas_height), color="black")

    # Merge the resized image onto the canvas with margins
    canvas.paste(resized_image, (left_margin, top_margin))

    # Calculate the font size based on canvas height
    # font_size = int(canvas_height * 0.02)  # Adjust the scaling factor as needed
    font_size = 24

    # Add text overlay
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(font_path, font_size)

    # Adjust the y-coordinate for proper alignment
    text_position = (left_margin, canvas_height - bottom_margin + font_size)

    draw.text(text_position, text_content, fill="white", font=font)

    # Generate the new file name
    file_name_parts = os.path.splitext(file_name)[0].split(".")
    new_file_name = file_name_parts[0] + f".{new_width}x{new_height}.jpg"

    # Save the processed image as JPEG
    output_path = os.path.join(output_directory, new_file_name)
    canvas.save(output_path, format="JPEG", quality=100)

    # log the successfull processing of the image
    print(f"Image {new_file_name} processed successfully.")

    # Close the image
    image.close()

print("Image processing completed.")
