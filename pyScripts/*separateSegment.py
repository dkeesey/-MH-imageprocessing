import os

def separate_segment(file_name):
    # Split the file name into segments
    file_name_parts = file_name.split(".")
    new_file_name = file_name_parts[0] + ".tif"

    # Save the image with the new file name
    os.rename(file_name, new_file_name)

    print(f"Image '{file_name}' renamed as '{new_file_name}'.")


if __name__ == "__main__":
    # Set the directory path
    directory = "./"

    # Get a list of files in the directory
    file_list = os.listdir(directory)

    # Loop through each file in the directory
    for file_name in file_list:
        # Check if the file is a TIFF image
        if file_name.lower().endswith(".tif"):
            # Separate the segment after the first dot in the file name
            separate_segment(file_name)
