# No-frills version of metadata-writer.py
# prints to the terminal and creates a .csv in the same folder as the images

# import needed libraries
from exif import Image
import os

folderPath = 'D:\Documents\Python\photo-metadata\TestPhotos' # the folder containing the images
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
print('File name, Shutter Speed, ISO, f-stop, focal length')

with open(os.path.join(folderPath, 'metadata.csv'), 'w') as output:
    print('File name, Shutter Speed, ISO, f-stop, focal length', file=output)

# for each image, print desired exif data
for file in filtered_files:
    filePath = os.path.join(folderPath, file)
    with open(filePath, 'rb') as image_file:
        thisImage = Image(image_file)
    exposure_fraction = '1/' + str(1/thisImage.exposure_time)

    data_to_print = [file, exposure_fraction, thisImage.photographic_sensitivity, thisImage.f_number, thisImage.focal_length]

    print(*data_to_print, end=", ")
    
    with open(os.path.join(folderPath, 'metadata.csv'), 'w') as output:
        print(*data_to_print, sep=', ', file=output)