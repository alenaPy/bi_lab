"""Labwork6."""

import csv
import gzip
import io
import json
import os
import requests
import zipfile

exs_file = os.path.isfile("restaurant-and-market-health-inspections.csv")

if not exs_file:
    file_url = "https://www.kaggle.com/cityofLA/" \
               "la-restaurant-market-health-data/downloads" \
               "/la-restaurant-market-health-data.zip/22"
    file_get = requests.get(file_url)
    data = zipfile.ZipFile(io.BytesIO(file_get.content))
    data.extractall()
    data.close()

    file_data = []

with open("restaurant-and-market-health-inspections.csv") as file_csv:
    file_csv_r = csv.reader(file_csv)
    for data_row in file_csv:
        file_data.append(data_row)
        print(data_row + "\n")


json_url = "https://www.kaggle.com/chicago/" \
           "chicago-red-light-and-speed-camera-data/downloads" \
           "/socrata_metadata_red-light-camera-locations.json/46"
json_get = requests.get(json_url)
with gzip.open(io.BytesIO(json_get.content), "r") as data:
    file = json.loads(data.read())
print(file)
