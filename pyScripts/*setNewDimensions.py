import os
from PIL import Image

def update_filename_with_dimensions(file_path):
    # Get the directory, filename, and extension
    directory = os.path.dirname(file_path)
    filename, extension = os.path.splitext(os.path.basename(file_path))

    # Split the filename by "."
    segments = filename.split(".")

    # Get the width and height from the last segment
    last_segment = segments[-1]
    width_height = last_segment.split("x")
    width = width_height[0]
    height = width_height[1]

    # Get the new filename with updated dimensions
    new_filename = ".".join(segments[:-1]) + f".{width}x{height}{extension}"

    # Generate the new file path
    new_file_path = os.path.join(directory, new_filename)

    # Rename the file
    os.rename(file_path, new_file_path)

    print(f"Renamed: {file_path} to {new_file_path}")

if __name__ == "__main__":
    # Specify the directory containing the JPG files
    directory = "./"

    # Get a list of files in the directory
    file_list = [file for file in os.listdir(directory) if file.lower().endswith(".jpg")]

    # Loop through each JPG file and update the filename
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        update_filename_with_dimensions(file_path)
