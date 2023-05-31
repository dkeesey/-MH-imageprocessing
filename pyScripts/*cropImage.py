import sys
import os
from PIL import Image

def crop_image(image_path, crop_values):
    # Open the image
    image = Image.open(image_path)

    # Crop the image using the provided crop values
    if len(crop_values) == 1:
        # Crop all sides by the same value
        image = image.crop((crop_values[0], crop_values[0], image.width - crop_values[0], image.height - crop_values[0]))
    elif len(crop_values) == 4:
        # Crop each side separately
        image = image.crop((crop_values[3], crop_values[0], image.width - crop_values[1], image.height - crop_values[2]))

    # Save the cropped image with the same file name
    file_name = os.path.basename(image_path)
    file_name_parts = file_name.split(".")
    new_file_name = file_name_parts[0] + ".tif"
    image.save(new_file_name)

    print(f"Image '{image_path}' cropped and saved as '{new_file_name}'.")


if __name__ == "__main__":
    # Get the script arguments (excluding the script name itself)
    args = sys.argv[1:]

    # Check the number of arguments
    if len(args) < 2:
        print("Usage: python *cropImage.py <image_file> <crop_values>")
        print("Crop Values:")
        print("  - Provide a single value to crop all sides by the same amount.")
        print("  - Provide four values separated by spaces for individual side cropping (top, right, bottom, left).")
        sys.exit(1)

    # Get the image file path and crop values
    image_file = args[0]
    crop_values = [int(value) for value in args[1:]]

    # Crop the image
    crop_image(image_file, crop_values)
