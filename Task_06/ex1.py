"""Ex1."""

import argparse
import csv
from dicttoxml import dicttoxml
import json
import os
import requests
import sys
import yaml


def dload(url):
    """Download a file via a URL, return file descriptor."""
    try:
        req = requests.get(url)
        file_name = url.rsplit('/', 1)[1]
    except Exception:
        print('URL or connection error has occurred')
        parser.print_help()
    else:
        if os.path.isfile(file_name):
            print('The file already exists')
        else:
            with open(file_name, 'wb') as le_file:
                le_file.write(req.content)
            print('The file has been successfully downloaded')
            file_name
            return file_name


rank = []
film = []
year = []
try:
    with open('ratings.list',
              'r', encoding='ISO-8859-1') as top250:
        i = 0
        films = []
        for line in top250:
            if 'New  Distribution  Votes  Rank  Title' in line:
                break
        for line in top250:
            if i >= 250:
                break
            else:
                rank.append(line.strip().split('  ')[2].lstrip())
                film.append(line.strip().rstrip(')').split('  ')[3]
                            .split(' (')[0])
                year.append(line.strip().rstrip('/I)').split('  ')[3]
                            .split(' (')[1])
                i += 1
except FileNotFoundError:
    print('The file hasn\'t been found')


# data for xml|json|yaml
data = []
for i in range(len(film)):
    data.append({"Id": str(i + 1), "Film": film[i], "Year": str(year[i]),
                 "Rating": str(rank[i])})

parser = argparse.ArgumentParser(description="Download and conversion are"
                                             "available")

parser.add_argument('--download', help='download a file using given VALID url')
parser.add_argument('--format', help='csv | json | xml | yaml')

args = parser.parse_args()

if args.download:
    dload(args.download)
if args.format == 'csv':
    dat = []
    dat.append('ID;Film;Year;Rating')
    for i in range(len(film)):
        dat.append(str(i + 1) + ';' + film[i] + ';' +
                   str(year[i]) + ';' + str(rank[i]))
    csv_dat = csv.reader(dat, delimiter=';')
    for row in csv_dat:
        print(';'.join(row))
if args.format == 'json':
    json_dat = json.dumps(data)
    print(json_dat)
if args.format == 'xml':
    xml_dat = dicttoxml(data, custom_root='root', attr_type=False)
    print(xml_dat)
if args.format == 'yaml':
    yaml_dat = yaml.safe_dump(data, explicit_start=True,
                              default_flow_style=False)
    print(yaml_dat)
if len(sys.argv) == 1:
    # zip_url = 'http://spatialkeydocs.s3.amazonaws.com/
    # FL_insurance_sample.csv.zip'
    # gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
    dload('https://wiki.mozilla.org/images/f/ff/Example.json.gz')
