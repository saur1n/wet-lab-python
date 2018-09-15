#!/usr/bin/env python

from PIL import Image
import os, sys

def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    
for file in os.listdir(sys.argv[1]):
    if file.endswith(".JPG"):
        crop(sys.argv[1]+file, (0,0,5000,3400), sys.argv[1]+file)