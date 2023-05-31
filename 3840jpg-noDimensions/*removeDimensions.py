import os

def remove_dimension_segment(directory):
    # Get a list of files in the directory
    file_list = [file for file in os.listdir(directory) if file.lower().endswith(".jpg")]

    # Loop through each JPG file
    for file_name in file_list:
        # Split the filename and extension
        name, extension = os.path.splitext(file_name)

        # Split the filename segments by '.'
        segments = name.split(".")

        # Check if the filename has a dimension segment
        if len(segments) > 1 and "x" in segments[-1]:
            segments = segments[:-1]

        # Reconstruct the new filename
        new_file_name = ".".join(segments) + extension
        new_file_path = os.path.join(directory, new_file_name)

        # Rename the file with the new filename
        os.rename(os.path.join(directory, file_name), new_file_path)

        print(f"Renamed: {file_name} to {new_file_name}")

if __name__ == "__main__":
    # Specify the directory containing the JPG files
    directory = "./"

    # Remove the dimension segment from filenames
    remove_dimension_segment(directory)
