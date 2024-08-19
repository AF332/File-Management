"""os module imported to interact with the operating system. Path class taken from the pathlib module
is used for easier file path manipulation."""
import os
from pathlib import Path

"""The keys of the dictionary is used to store the dirctories names, while the dictionary's values
are lists of file extensions associated with that directory."""
SUBDIRECTORIES = {
    "MODEL SAVED": ['.pb'],
    "EXCEL": ['.xlsx'],
    "PYTHON SCRIPT": ['.ipynb', '.py'],
    "MODEL IMAGES & MASKS": ['.dcm', '.nii', '.gz'],
    "MODEL VARIABLES": ['.data-00000-of-00001'],
    "REHABILITATION SOFTWARE": ['.acq', '.jcq', '.file'],
    "LECTURES & PAPERS": ['.pdf'],
    "DOCUMENTS": ['.docx', '.txt'],
    "POWERPOINT": ['.pptx'],
    "AUDIO": ['.m4a', '.m4b', '.mp3', '.wav'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}

"""This function determines the appropriate directroy for a given file extension."""
def pickDirectory(value):
    for category, extensions in SUBDIRECTORIES.items(): # iterates over the 'SUBDIRECTORIES' dictionary, unpacking each key-value pair into 'category' and 'suffixes'.
        for suffix in extensions: # Iterates over each suffix in the list of 'extensions'
            if suffix == value: # checks if the current suffix matches the file extension 'value' passed to the function.
                return category # If the condition is met, the function returns the name of the category (directory name).
    return 'MISC' # If no matching suffix is found, the function defaults to returning 'MISC', categorising the file as miscellaneous.

"""This function is designed to organise files in the current directory"""
def organiseDirectory():
    for item in os.scandir(): # Use 'os.scandir()' to iterate through entries in the current directory.
        if item.is_dir(): # Skips the iteration if the 'item' is a directory.
            continue
        filePath = Path(item) # Converts the directory entry 'item' to a 'Path' object for easier handling.
        fileType = filePath.suffix.lower() # Extracts the file extension from 'filePath' and converts it to lowercase.
        directory = pickDirectory(fileType) # Calls 'pickDirectory' to determine the appropriate directory based on the file extension.
        directoryPath = Path(directory) # Converts the directory name into a 'Path' object.
        if directoryPath.is_dir() != True: # Checks if the directory exist, and if not, creates it.
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath)) # 'filePath.rename' is used to move the file. The 'joinpath' method is used to construct the new path by combining the directory path with the original file path.

organiseDirectory() # Calls the function to running the program.