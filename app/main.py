#!/usr/bin/env python3

import os
import argparse
from PIL import Image


def flip_resize_image(imagePath: str, outputFileImage: str,
                      rotateAngle: int, resizeHeight: int = None,
                      resizeWidth: int = None):
    with Image.open(imagePath) as im:
        newImage = im.rotate(rotateAngle)
        if resizeHeight and resizeWidth:
            newImage = newImage.resize((resizeWidth, resizeHeight))
        newImage.save(outputFileImage)
        print(f"*** image saved at {outputFileImage}")


def verify_image_extension(imagePath: str):
    _, imageExt = os.path.splitext(imagePath)
    if imageExt not in (".jpg", ".jpeg", ".png"):
        raise RuntimeError("Kindly provide a valid image.")


def get_output_file_name(ipImage: str):
    imageName, imageExt = os.path.splitext(ipImage)
    return f"{imageName}_updated.jpg"


def parse_cmdline():
    parser = argparse.ArgumentParser(
        description="A command line utility for"
                    "manipulating images.")
    parser.add_argument("-ip", "--input_image", dest="ip_image",
                        help="Absolute path to the input image.")
    parser.add_argument("-op", "--output_image", dest="op_image",
                        default=None,
                        help="Path to the output image.")
    parser.add_argument("-ro", "--rotate", dest="rotate",
                        type=int, default=360,
                        help="Rotate image by an angle.")
    parser.add_argument("-rsh", "--resize_height", dest="rs_height",
                        type=int, help="Resize image Height")
    parser.add_argument("-rsw", "--resize_width", dest="rs_width", 
                        type=int, help="Resize image Width")

    args = parser.parse_args()
    return args


def main():
    args = parse_cmdline()
    verify_image_extension(args.ip_image)
    opImagePath = args.op_image or get_output_file_name(args.ip_image)
    flip_resize_image(args.ip_image, opImagePath, args.rotate,
                      args.rs_height, args.rs_width)


if __name__ == "__main__":
    main()
