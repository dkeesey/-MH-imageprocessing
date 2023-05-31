import os
from PIL import Image

def resize_and_save_as_jpg(file_path, output_directory):
    # Open the image
    image = Image.open(file_path)

    # Calculate the new width based on the desired maximum width
    max_width = 3840
    width_ratio = max_width / image.width
    new_width = max_width
    new_height = int(image.height * width_ratio)

    # Resize the image with Lanczos filter
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Save the resized image as JPG with the highest quality
    output_file = os.path.join(output_directory, os.path.splitext(os.path.basename(file_path))[0] + ".jpg")
    resized_image.save(output_file, "JPEG", quality=100)

    print(f"Resized and saved: {output_file}")

if __name__ == "__main__":
    # Specify the directory containing the TIFF files
    input_directory = "./"

    # Specify the output directory for the JPG files
    output_directory = "jpg-output"

    # Get a list of files in the input directory
    file_list = [file for file in os.listdir(input_directory) if file.lower().endswith(".tif")]

    # Loop through each TIFF file and resize it
    for file_name in file_list:
        file_path = os.path.join(input_directory, file_name)
        resize_and_save_as_jpg(file_path, output_directory)
