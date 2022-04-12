#!/usr/bin/env python

import os
from pathlib import Path
from PIL import Image


def flip_resize_image(imagePath, outputFileImage):
    im = Image.open(imagePath)
    rotated = im.rotate(90)
    resized = rotated.resize((640, 480))
    resized.save(outputFileImage)
    print("image saved")



imagesPath = os.path.join(Path(os.getcwd()).parent, "data")

def main():
    for pos, item in enumerate(os.listdir(imagesPath)):
        if not (item.endswith("jpg") or item.endswith("jpeg")):
            continue

        imagePath = os.path.join(imagesPath, item)
        imageName, imageExt = os.path.splitext(imagePath)
        outputFileImage = f"{imageName}_{pos+1}.jpg"
        flip_resize_image(imagePath, outputFileImage)

if __name__ == "__main__":
    main()