#!/usr/bin/env python

"""Exported SVG files have width and height set to 100% and can appear very large.

This script finds all SVG files in a directory ands sets their height to a fixed size of
20px (the original design intent). Runs in Python 2 or 3.

NOTE: Files will be overwritten in place!
"""

from os import listdir
from os.path import isfile, join, realpath, isdir
import sys


if ('-h' in sys.argv or '--help' in sys.argv):
    print("Usage: set_fixed_height.py input_directory \n \
    Files will be overwritten in place!")
    sys.exit(0)

if len(sys.argv) < 2:
    sys.exit("Input directory is required. Usage: set_fixed_height.py input_directory")

in_path = realpath(sys.argv[1])

if not isdir(in_path):
    sys.exit("Given input_directory is not a directory")

print("Checking for .svg files at {}".format(in_path))

only_svg_files = [join(in_path, f) for f in listdir(in_path) if isfile(join(in_path, f)) and f.endswith('.svg')]

for filename in only_svg_files:
    with open(filename, 'r+') as f:
        print("Replacing height for {}".format(filename))
        data = f.read()
        output = data.replace('<svg width="100%" height="100%"', '<svg width="100%" height="20px"', 1)
        f.seek(0)
        f.write(output)
        f.truncate()

print("Operation Complete.")
