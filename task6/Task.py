"""Task6."""

import argparse
import csv
import gzip
import io
import json
import os
import requests
import urllib.request
import xml.etree.cElementTree as ET
import yaml
import zipfile

parser = argparse.ArgumentParser()

parser.add_argument("--download", help="Provide downloading of files",
                    action="store_true")
parser.add_argument("--format",
                    help='Use json | xml | csv | yaml'
                    ' to convert to choosen format')

arguments = parser.parse_args()


exists = os.path.isfile('arch.zip')


def get_zip():
    """Download zip archive."""
    urllib.request.urlretrieve(
        'https://github.com/ZhenyaBond/123/raw/master/arch.zip', 'arch.zip')
    print("Downloaded successfully.")


def read_zip():
    zip_f = zipfile.ZipFile('arch.zip')
    zip_f.extractall()
    zip_f.close()

    with open("countries of the world.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)


def get_gz():
    """Read json data."""
    gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
    gz_get = requests.get(gz_url)
    with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
        file = json.loads(data.read())
    print("This is content of JSON file: {0}".format(file))


if arguments.download:
    if not exists:
        get_zip()
    else:
        print("File exists.")

if arguments.format == 'json':
    with open('countries of the world.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('json_format.json', 'w') as f:
        json.dump(rows, f)
    print("json created.")

if arguments.format == 'xml':
    with open('countries of the world.csv') as f:
        text = f.readlines()

    root = ET.Element('root')
    root.text = str(text)
    tree = ET.ElementTree(root)
    tree.write('xml-format.xml')
    print("xml-created.")

if arguments.format == 'csv':
    with open('countries of the world.csv') as f:
        csvreader = csv.reader(f)
        text = []
        for row in csvreader:
            text += row

    with open('csv-format.csv', 'w') as csv_f:
        csv_writer = csv.writer(csv_f)
        csv_writer.writerow(text)
    print("scv created.")

if arguments.format == 'yaml':
    with open('countries of the world.csv') as csv_f:
        csvreader = csv.reader(csv_f)
        text = []
        for row in csvreader:
            text += row

    with open('yaml-format.yaml', 'w') as f:
        yaml.dump(text, f, default_flow_style=False)
    print('yaml created.')
