#!/usr/bin/env python3

import os


def parse_description(fruitFile):
    with open(fruitFile, 'r') as file:
        description = file.read()
        # First line is the fruit name
        fruit_name = description.splitlines()[0].strip()
        # Second line is the weight, It can be a string
        weight_line = description.splitlines()[1].strip()
        # Third line is the description
        fruit_description = description.splitlines()[2].strip()
        # the image name
        image_name = fruit_name.lower() + ".jpg"

    # Parse into a json-like dictionary
    fruit_info = {
        "name": fruit_name,
        "weight": float(weight_line.split()[0]), # Extract the numeric part of the weight
        "description": fruit_description,
        "image name": image_name # Add the image name to the dictionary
    }

    return fruit_info

if __name__ == "__main__":

    # Get the directory where ParsingDescription.py actually lives
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level from 'Utils' to find 'Fruit_Images'
    Folder_path = os.path.join(base_dir, '..', 'Fruit_Images')
    # Loop through the .txt files in the folder and parse them
    for filename in os.listdir(Folder_path):
        if filename.lower().endswith('.txt'):
            fruit_info = parse_description(os.path.join(Folder_path, filename))
            print(fruit_info)
