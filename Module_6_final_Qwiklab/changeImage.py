#!/usr/bin/env python3

# 1) Working with supplier images: change size (from 3000x2000 to 600x400) and format (from .tiff to .jpeg)
import glob
from PIL import Image
import os, sys

#Change the dir to supplier-data/images/
os.chdir("supplier-data/images/")
print("Stage 1: check current dir: {}".format(os.getcwd()))
lista = []
for infile in glob.glob("*.tiff"):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpeg"
    try:
      im = Image.open(infile).convert("RGB")
      im.thumbnail((600,400))
      im.save(outfile, "JPEG")
    except OSError as e:
      print("Cannot convert because: {}".format(e))