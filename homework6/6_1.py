"""Import."""

import csv

import io

import json

import os

import requests

import gzip

import zipfile


# zip file

exists = os.path.isfile('ext_services.csv')

if not exists:

    zip_url = 'https://github.com/NatalliaBaranava/bi_lab/raw/' \
              'homework6/homework6/my_archieve.zip'

    zip_get = requests.get(zip_url)

    data = zipfile.ZipFile(io.BytesIO(zip_get.content))

    data.extractall()

    data.close()


list1 = []

with open('ext_services.csv', encoding='UTF-8') as cur:
    csv_rd = csv.reader(cur)
    for row in csv_rd:
        list1.append(row)
        print(str(row) + '\n')


# gzipped json file

gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'

gz_get = requests.get(gz_url)

with gzip.open(io.BytesIO(gz_get.content), 'r') as data:

    file = json.loads(data.read())

print(file)
