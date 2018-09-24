"""Labwork6."""

import argparse
from collections import OrderedDict
import csv
import gzip
import io
import json
import os
import requests
import yaml
import zipfile


parser = argparse.ArgumentParser()
parser.add_argument('--format', default=False)
parser.add_argument('--download', action="store_true",default=False)
arguments = parser.parse_args()

# zip file
if arguments.download:
    exists = os.path.isfile('CAS.WDC11019.NA11.FINAL.DT11186.TXT')
    if not exists:
        zip_url = 'https://www.fsa.usda.gov/Internet/FSA_File/2011_name_' \
                  'address_file.zip'
        zip_get = requests.get(zip_url)
        data = zipfile.ZipFile(io.BytesIO(zip_get.content))
        data.extractall()
        data.close()
    list = []
    with open('CAS.WDC11019.NA11.FINAL.DT11186.TXT') as filee:
        for row in filee:
            list.append(row)
            print(row + '\n')



# data serialization
csv_file = 'programs.csv'

# zip file
exists = os.path.isfile(csv_file)
if not exists:
    zip_url = 'https://github.com/SimonenkoV/bi_lab/raw/Exit_Task/' \
              'exit_task/programs.zip'
    zip_get = requests.get(zip_url)
    data = zipfile.ZipFile(io.BytesIO(zip_get.content))
    data.extractall()
    data.close()
    print('zip archive extracted')
else:
    print('data file ' + csv_file + ' already exists')

# Check arguments

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
        "CATEGORY_CODE", "CATEGORY_NAME", "PROGRAM_CODE", "COMMODITY_CODE",
        "COMMODITY_NAME", "PROGRAM_NAME")
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


# to yaml
if arguments.format == 'yaml':
    in_file = open(csv_file, "r")
    out_file = open('yaml_file.yaml', "w")
    items = []

    def convert_to_yaml(line):
        """Convert to yaml."""
        item = {
            'CATEGORY_CODE': line[0],
            'CATEGORY_NAME': line[1],
            'PROGRAM_CODE': line[2],
            'COMMODITY_CODE': line[3],
            'COMMODITY_NAME': line[4],
            'PROGRAM_NAME': line[5],
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


# gzipped json file
gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = requests.get(gz_url)
with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())
print(file)
