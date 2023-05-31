import os
from PIL import Image


def add_dimension_segment(file_path):
    # Open the image and get its width and height
    image = Image.open(file_path)
    width, height = image.size

    # Split the file name and extension
    file_name, file_extension = os.path.splitext(file_path)

    # Create the dimension segment
    dimension_segment = f"{width}x{height}"

    # Construct the new file name with the dimension segment
    new_file_name = f"{file_name}.{dimension_segment}{file_extension}"

    # Rename the file with the new file name
    os.rename(file_path, new_file_name)

    print(f"File '{file_path}' renamed to '{new_file_name}'.")


if __name__ == "__main__":
    # Get the current directory
    directory = os.getcwd()

    # Get a list of files in the directory
    file_list = [file for file in os.listdir(
        directory) if os.path.isfile(os.path.join(directory, file))]

    # Loop through each file in the directory
    for file_name in file_list:
        # Check if the file is an image file
        if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff")):
            # Add the dimension segment to the file name
            add_dimension_segment(file_name)
