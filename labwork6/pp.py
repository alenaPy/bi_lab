"""Ex1."""
import csv
import io
import json
import os
import requests
import gzip
import zipfile


# zip file
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


# gzipped json file
gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = requests.get(gz_url)
with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())
print(file)

