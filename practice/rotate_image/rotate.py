"""a basic program that takes a .jpg file and rotates it"""

# Imports:
from PIL import Image
import sys


def rotate(delta):
    "Roll an image sideways"
    im = Image.open(sys.argv[1])
    out = im.rotate(delta)
    out.save(sys.argv[2])


def main():
    """main"""
    rotate(180)


main()
