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
    imageName = image.split('.')[0]
    extension = image.split('.')[1]
    img = Image.open(image)
    img.save(imageName+'-compressed'+ '.' + extension,
             optimize=True,
             quality=quality)
