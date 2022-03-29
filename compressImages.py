from PIL import Image
import PIL
import os
import glob

# pathToJPGs = os.getcwd()+"/dropImagesHere/"
os.chdir("dropImagesHere")
images = [file for file in os.listdir() if file.endswith(('jpg', 'png', 'jpeg' ))]

# VARIABLE
quality = 30 # The image quality, on a scale from 0 (worst) to 95 (best). The default is 75. Values above 95 should be avoided; 100 disables portions of the JPEG compression algorithm, and results in large files with hardly any gain in image quality.



for image in images:
    if (image.count(".") == 1):
        imageName = image.split('.')[0]
        extension = image.split('.')[1]
        print(extension)
        img = Image.open(image)
        img.save(imageName+'-compressed'+ '.' + extension,
                 optimize=True,
                 quality=quality)
    elif (image.count(".") > 1):
        print("The name " + image + " has more than 1 full stop. Rename it so that it only has 1 full stop.")

    elif (image.count(".") == 0):
        print("The name " + image + " has no full stop. Make sure there is extension in this file.")

