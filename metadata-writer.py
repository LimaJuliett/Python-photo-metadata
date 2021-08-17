# Creates a .csv in the same folder as the images, with option to print out to console

print('Hi! I\'m a Python script that will generate a .csv file with some of the metadata from pictures in whatever folder you put me in.\nI won\'t search recursively (i.e. I can\'t see pictures in subfolders).\nTo modify what metadata I print, please see line 42 of my code (data_to_print), and the exif docs (https://pypi.org/project/exif/). You will also need to modify the field names (line 27).\n')
print_to_console = input('Do you want me to also print metadata information to the console? (y/N): ')
print() # print a newline for neatness

# import needed libraries
from exif import Image
import os

folderPath = os.getcwd() # the folder containing the images
fileArray = os.listdir(folderPath) # an array of all images in the folder
allowed_file_types = ['.jpg', '.jpeg', '.tiff', '.png', '.bmp', '.gif'] # these are the only files that will be recognized

# function to filter out anything that doesn't end with an allowed file type
def allowed_files_filter(name):
    for extension in allowed_file_types:
        if (name.lower().endswith(extension)):
            return True
        else:
            return False

filtered_files = filter(allowed_files_filter, fileArray) # filter out files not ending in allowed file types

# print field names
if (print_to_console == 'y'):
    print('File name, Shutter Speed, ISO, f-stop, focal length')

with open(os.path.join(folderPath, 'metadata.csv'), 'w') as output_file:
    print('File name, Shutter Speed, ISO, f-stop, focal length', file=output_file)

# for each image, print desired exif data
for file in filtered_files:
    # open file
    filePath = os.path.join(folderPath, file)
    with open(filePath, 'rb') as image_file:
        thisImage = Image(image_file)
    
    # make exposure human-readable
    exposure_fraction = '1/' + str(1/thisImage.exposure_time)

    data_to_print = [file, exposure_fraction, thisImage.photographic_sensitivity, thisImage.f_number, thisImage.focal_length]
    # print metadata
    if (print_to_console == 'y'):
        print(*data_to_print, sep=', ')
    
    with open(os.path.join(folderPath, 'metadata.csv'), 'a') as output_file:
        print(*data_to_print, sep=', ', file=output_file)

input('\nThanks for letting me run! I hope I was helpful. For more information see https://github.com/LimaJuliett/Python-photo-metadata.\n\nPress enter to exit.')