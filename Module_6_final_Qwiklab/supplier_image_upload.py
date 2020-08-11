#!/usr/bin/env python3

import requests
import glob
import os

# Module for uploading images to web server
# Useful: dest = os.path.join(os.getcwd(), "/supplier-data/images")

url = "http://localhost/upload/"
os.chdir("supplier-data/images/")
for filepath in glob.glob("*.jpeg"):
    with open(filepath, 'rb') as opened:
        r = requests.post(url, files={'file': opened})