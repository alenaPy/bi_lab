"""Import."""
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
parser.add_argument("--format",
                    help='Use json | xml | csv | yaml'
                    ' to convert to chosen format')
arguments = parser.parse_args()

# zip file
exists = os.path.isfile('2018.csv')
if not exists:
    zip_url = 'https://github.com/YauheniyaZaitsava/bi_lab-1/' \
              'raw/Homework7/movies.zip'
    zip_get = requests.get(zip_url)
    data = zipfile.ZipFile(io.BytesIO(zip_get.content))
    data.extractall()
    data.close()

list1 = []
with open('movies.csv', encoding='ISO-8859-1') as cur:
    csv_rd = csv.reader(cur)
    for row in csv_rd:
        list1.append(row)
        print(row + '\n')


# gzipped json file
gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = requests.get(gz_url)
with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())
print(file)


# 4 formats
exists = os.path.isfile('movies.csv')


def get_zip():
    """DownloadZipArchive."""
    urllib.request.urlretrieve(
        'https://github.com/YauheniyaZaitsava/bi_lab-1/'
        'raw/Homework7/movies.zip', 'movies.zip')
    print("Download is completed successfully.")


get_zip()


def read_zip():
    """ReadZip."""
    try:
        zip_file = zipfile.ZipFile('movies.zip')
        zip_file.extractall()
        zip_file.close()
    except zipfile.BadZipFile:
        print('Zip file was not loaded')
    else:
        print('Loaded successfully')


read_zip()


if arguments.format == 'json':
    with open('movies.csv', encoding='ISO-8859-1') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
    with open('json_format.json', 'w') as csv_file:
        json.dump(rows, csv_file)
    print("Json created.")


if arguments.format == 'xml':
    with open('movies.csv', encoding='ISO-8859-1') as csv_file:
        text = csv_file.readlines()
    root = ET.Element('root')
    root.text = str(text)
    tree = ET.ElementTree(root)
    tree.write('xml-format.xml')
    print("Xml created.")


if arguments.format == 'csv':
    with open('movies.csv', encoding='ISO-8859-1') as csv_file:
        csvreader = csv.reader(csv_file)
        text = []
        for row in csvreader:
            text += row
    with open('csv-format.csv', 'w') as csv_f:
        csv_writer = csv.writer(csv_f)
        csv_writer.writerow(text)
    print("Csv created.")


if arguments.format == 'yaml':
    with open('movies.csv') as csv_f:
        csvreader = csv.reader(csv_f)
        text = []
        for row in csvreader:
            text += row
    with open('yaml-format.yaml', 'w') as f:
        yaml.dump(text, csv_file, default_flow_style=False)
    print('yaml created.')
