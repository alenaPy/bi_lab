"""Task6."""

from csv import reader
from requests import get
from io import BytesIO
from zipfile import ZipFile
from os import path
import json
import gzip


exists = path.isfile("countries of the world.csv.csv")

if not exists:
    request = get("https://github.com/ZhenyaBond/123/raw/master/arch.zip")
    zip_file = ZipFile(BytesIO(request.content))
    zip_file.extractall()
    zip_file.close()

    with open("countries of the world.csv", 'r') as csvfile:
        csvreader = reader(csvfile)
        for row in csvreader:
            print(row)

gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
gz_get = get(gz_url)
with gzip.open(BytesIO(gz_get.content), 'r') as data:
    file = json.loads(data.read())

print("This is content of JSON file: {0}".format(file))