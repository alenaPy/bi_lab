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
    zip_url = 'http://spatialkeydocs.s3.amazonaws.com/' \
              'FL_insurance_sample.csv.zip'
    zip_get = requests.get(zip_url)
    data = zipfile.ZipFile(io.BytesIO(zip_get.content))
    data.extractall()
    data.close()
    list = []

with open('FL_insurance_sample.csv') as csvfile:
    csv_rd = csv.reader(csvfile)
    for row in csv_rd:
        list.append(row)
        print(', '.join(row))
print('=' * 200)

# gzipped json file
gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = requests.get(gz_url)
with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())
print(file)
