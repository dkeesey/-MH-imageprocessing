import os

def add_suffix(file_name, suffix):
    # Check if the file already ends with the suffix
    if file_name.endswith(suffix):
        return file_name  # No change needed

    # Add the suffix to the file name
    new_file_name = file_name + suffix

    # Rename the file with the new file name
    os.rename(file_name, new_file_name)

    print(f"File '{file_name}' renamed as '{new_file_name}'.")


if __name__ == "__main__":
    # Set the directory path
    directory = "./"

    # Get a list of files in the directory
    file_list = os.listdir(directory)

    # Set the suffix
    suffix = ".tif"

    # Loop through each file in the directory
    for file_name in file_list:
        # Check if the file does not end with the suffix
        if not file_name.endswith(suffix):
            # Add the suffix to the file name
            add_suffix(file_name, suffix)
