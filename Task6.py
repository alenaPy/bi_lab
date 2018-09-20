"""Import."""
import csv
import io
import json
import os
import requests
import gzip
import zipfile


# zip file
exists = os.path.isfile('2018.csv')
if not exists:
    zip_url = 'https://github.com/YauheniyaZaitsava/bi_lab-1/raw/' \
              'Homework6/Currency.zip'
    zip_get = requests.get(zip_url)
    data = zipfile.ZipFile(io.BytesIO(zip_get.content))
    data.extractall()
    data.close()

list1 = []
with open('2018.csv', encoding='UTF-8') as cur:
    csv_rd = csv.reader(cur)
    for row in csv_rd:
        list.append(row)
        print(row + '\n')


# gzipped json file
gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = requests.get(gz_url)
with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())
print(file)
