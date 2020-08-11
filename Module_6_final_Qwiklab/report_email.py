#!/usr/bin/env python3

import os.path
import sys
import json
import reports
import datetime
from datetime import date
import emails


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

def generate_table_data(data, empty_line=reports.Spacer(1, 2)):
    table_data = []
    for item in data:
        table_data.append(["name" + ": " +  item["name"]])
        table_data.append(["weight" + ": " + item["weight"]])
        table_data.append([empty_line])
    return table_data

def process_supplier_data(path):
    folder = os.listdir(path)
    keys = ["name", "weight"]
    supplier_data = []
    for file in folder:
        with open(path + file) as txt_file:
            i = 0
            items = {}
            for line in txt_file.readlines()[:2]:
                items[keys[i]] = line.strip()
                i = i + 1
            supplier_data.append(items)
    return supplier_data

def generate_json(supplier_data):
    with open ('generator.json', 'w') as f:
        # Save i t to the json file 'generator.json'
        json.dump(supplier_data, f, indent=2)
        # Save it to the lista
        # json_list = json_dumps(supplier_data)
        filename = 'generator.json'
    return filename

def main(argv):
    # Generate the data for PDF creation
    path = os.getcwd() + "/supplier-data/descriptions/"
    filename = generate_json(process_supplier_data(path))
    data = load_data(filename)
    paragraph = generate_table_data(data)
    # TODO: turn this into a PDF report
    today = datetime.date.today()
    title = "Processed Update on {}".format(today.strftime("%B %d, %Y"))
    attachment_pth = "/tmp/processed.pdf"
    reports.generate_report(attachment_pth, title, paragraph )

    # TODO: send the PDF report as an attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploded to our website sucessfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, attachment_pth)
    emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)
