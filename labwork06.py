"""Labwork06."""
import csv
import gzip
import io
import json
import os
import requests
import zipfile

# zip file
exists = os.path.isfile('FL_insurance_sample.csv')
if not exists:
    zip_url = 'https://github.com/natalliahaisionak/Files/raw/master/6.zip'
zip_get = requests.get(zip_url)
data = zipfile.ZipFile(io.BytesIO(zip_get.content))
data.extractall()
data.close()
new_list = []

with open('table.csv') as csv_file:
    csv_rd = csv.reader(csv_file)
    for row in csv_rd:
        new_list.append(row)
        print(', '.join(row))

# gzipped json file
gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = requests.get(gz_url)
with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())

print(file)
