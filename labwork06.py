"""Labwork06."""
import argparse
import csv
import gzip
import io
import json
import os
import requests
import yaml
import zipfile
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument('--format', default=False)
arguments = parser.parse_args()
csv_file = 'table.csv'

# zip file
exists = os.path.isfile(csv_file)
if not exists:
    zip_url = 'https://github.com/natalliahaisionak/Files/raw/master/6.zip'
    zip_get = requests.get(zip_url)
    data = zipfile.ZipFile(io.BytesIO(zip_get.content))
    data.extractall()
    data.close()
    print('zip archive extracted')
else:
    print('data file ' + csv_file + ' exists')

# to csv
if arguments.format == 'csv':
    with open(csv_file) as file:
        csv_rd = csv.reader(file)
        with open('csv_output.csv', 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            for row in csv_rd:
                writer.writerow(row)
                print(', '.join(row))


# to JSON
if arguments.format == 'json':
    fieldnames = (
        "SERVICE_STATION", "ADDR", "POST", "STREET", "BUILDING", "CITY_ID",
        "CITY",
        "COUNTRY", "CODE")
    entries = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            entry = OrderedDict()
            for field in fieldnames:
                entry[field] = row[field]
            entries.append(entry)
    output = {"Service": entries}
    with open('file.json', 'w') as jsonfile:
        json.dump(output, jsonfile)
        jsonfile.write('\n')

# to XML
if arguments.format == 'xml':
    csvData = csv.reader(open(csv_file))
    xmlData = open('xmlData.xml', 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    xmlData.write('<csv_data>' + "\n")
    rowNum = 0
    for row in csvData:
        if rowNum == 0:
            tags = row
        else:
            xmlData.write('<row>' + "\n")
            for i in range(len(tags)):
                xmlData.write('    ' + '<' + tags[i] + '>' +
                              row[i] + '</' + tags[i] + '>' + "\n")
            xmlData.write('</row>' + "\n")
        rowNum += 1
    xmlData.write('</csv_data>' + "\n")
    xmlData.close()

# to yaml
if arguments.format == 'yaml':
    in_file = open(csv_file, "r")
    out_file = open('yaml_file.yaml', "w")
    items = []

    def convert_to_yaml(line):
        """Convert to yaml."""
        item = {
            'SERVICE_STATION': line[0],
            'ADDR': line[1],
            'POST': line[2],
            'STREET': line[3],
            'BUILDING': line[4],
            'CITY_ID': line[5],
            'CITY': line[6],
            'COUNTRY': line[7],
            'CODE': line[8]
        }
        items.append(item)
    try:
        reader = csv.reader(open(csv_file, "r"))
        # skip headers
        next(reader)
        for i, line in enumerate(reader):
            convert_to_yaml(line)
        out_file.write(yaml.dump(items, default_flow_style=False))
    finally:
        in_file.close()
        out_file.close()


# gzipped json file
gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = requests.get(gz_url)
with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())
print(file)
