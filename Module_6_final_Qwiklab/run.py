#! /usr/bin/env python3

import os
import requests
import json

# TO DO: Generate description and upload to the server:
def generate_data_upload(path):
    folder = sorted(os.listdir(path))
    keys = ["name", "weight", "description", "image_name"]
    lista = []
    for file in folder:
        with open(path + file) as txt_file:
            i = 0
            items = {}
            for line in txt_file.readlines()[:3]:
                if keys[i] == "weight":
                    items[keys[i]] = int(line.strip()[:-4])
                else:
                    items[keys[i]] = line.strip()
                i = i + 1
            f, e = os.path.splitext(file)
            items[keys[3]] = f + ".jpeg"
            lista.append(items)
            #TO DO Uploading to the server with requests POST method:
            response = requests.post("http://[linux-instance-external-IP]/fruits/", data=items)
            # #run status code method
            if not response.ok:
                raise Exception("Get failed with status code".format(response.status_code))
            else:
                print("Response status code ok")

path = os.getcwd() + "/supplier-data/descriptions/"
generate_data_upload(path)
#Optional JSON solution - write to json file with list and save it
# with open ('test.json', 'w') as f:
    # Save i t to the json file 'test.json'
    # json.dump(lista, f, indent=2)
    # Save it to the lista
    # json_list = json_dumps(lista)
