#!/usr/bin/env python3
from PIL import Image
import os


def change_image(image, size, format, save_path):
    """
    Size: Change image resolution to 600x400 pixel
    format: change image format from jpg to png
    """
    print("Changing image...")
    try:
        with Image.open(image) as img:
            # Resize the image, it returns an image
            new_image = img.resize(size)
            # Convert the image to RGB format
            if new_image.mode != 'RGB' and format.lower() == 'jpeg':
                new_image = new_image.convert('RGB')
            # Save the image
            new_image.save(save_path, format)
            print("Image changed successfully.")
    except Exception as e:
        print(f"Failed to process {image}: {e}")


# Ensure the destination directory exists
if not os.path.exists("images"):
    os.makedirs("images")

# for each file in the Fruit_Images directory, if the file is a jpg, change it to png and save it in the images directory
for file in os.listdir("Fruit_Images"):
    if file.endswith(".jpg"):
        # Construct the full path to the source image
        source_path = os.path.join("Fruit_Images", file)
        # Safer extension replacement
        filename, _ = os.path.splitext(file)
        # Construct the full path to the destination image
        destination_path = os.path.join("images", filename + ".png")
        # Change the image
        change_image(source_path, (600, 400), "png", destination_path)
        
        
        

