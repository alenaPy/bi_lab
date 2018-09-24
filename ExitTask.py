"""ArgumentsProcessing."""
import argparse
import csv
import gzip
import io
import json
import os
import requests
import urllib.request
import xml.etree.cElementTree as ET
import yaml
import zipfile


parser = argparse.ArgumentParser()
parser.add_argument('--year', help='displays Top250 movie titles with year',
                    action='store_true')
parser.add_argument('--rate', help='displays Top250 movie titles with rate',
                    action='store_true')
parser.add_argument('--all', help='shows title, rate, year',
                    action='store_true')
parser.add_argument('--histogram', help='displays histogram for rating or for'
                    ' years (in text format)')
parser.add_argument('--output', help='stores all data to specified filename'
                    ' file')
parser.add_argument("--download", help="Provide downloading of files",
                    action="store_true")
parser.add_argument("--format",
                    help='Use json | xml | csv | yaml'
                    ' to convert to chosen format')

arguments = parser.parse_args()
all_data = []
try:
    count = 0
    with open('ratings.list', 'r', encoding='ISO-8859-1') as ratings:
        for line in ratings:
            if 'New  Distribution  Votes  Rank  Title' in line:
                break
        for line in ratings:
            if count < 250:
                title = line.strip().split('  ')[3].split('(')[0]
                rat = line.strip().split('  ')[2]
                year = line.strip().split('  ')[3].rstrip(')').split('(')[1]
                count += 1
                all_data.append([title, rat, year])
except FileNotFoundError:
    print('Not exists')

year = []
for y in range(250):
    year.append(all_data[y][2])
dict_year = dict((i, year.count(i)) for i in year)
print(year)

rating = []
for y in range(250):
    rating.append(all_data[y][1])
dict_rat = dict((i, rating.count(i)) for i in rating)
print(rating)


if arguments.year:
    print('Top250 movies titles with year')
    i = 0
    for y in all_data:
        i += 1
        print((str(i) + '. ' + y[0] + ' ' + y[1]))
if arguments.rate:
    print('Top250 movies titles with rate')
    i = 0
    for y in all_data:
        i += 1
        print((str(i) + '. ' + y[0] + ' ' + y[1]))
if arguments.histogram == 'rate':
    print('Rate histogram.')
    for y in dict_rat:
        print(str(y) + ' ' + '*' * dict_rat[y] + ' ' +
              str(dict_rat[y]))
elif arguments.histogram == 'year':
    print('Year histogram.')
    for y in dict_year:
        print(str(y) + ' ' + '*' * dict_year[y] + ' ' +
              str(dict_year[y]))
if arguments.all:
    print('Top250 movies. Title, rate, year')
    i = 0
    for y in all_data:
        i += 1
        print((str(i) + '. ' + y[0] + ' ' + y[2] + ' ' + y[1]))
if arguments.output:
    print(arguments.output)
    out_file = open(arguments.output, "w")
    i = 0
    for y in all_data:
        i += 1
        out_file.write((str(i) + '. ' + y[0] + ' ' + y[2] + ' ' +
                        y[1]) + '\n')
    out_file.close()

# zip file conversion
    exists = os.path.isfile('movies.csv')


def get_zip():
    """DownloadZipArchive."""
    urllib.request.urlretrieve(
        'https://github.com/YauheniyaZaitsava/bi_lab-1/'
        'raw/Homework7/movies.zip', 'movies.zip')
    print("Download is completed successfully.")


get_zip()


def read_zip():
    """ReadZip."""
    try:
        zip_file = zipfile.ZipFile('movies.zip')
        zip_file.extractall()
        zip_file.close()
    except zipfile.BadZipFile:
        print('Zip file was not loaded')
    else:
        print('Loaded successfully')


read_zip()
with open('movies.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
for row in csvreader:
        print(row)


def get_gz():
    """ReadJsonData."""
    gz_url = 'https://wiki.mozilla.org/images/f/ff/Example.json.gz'
    gz_get = requests.get(gz_url)
    with gzip.open(io.BytesIO(gz_get.content), 'r') as data:
        file = json.loads(data.read())
    print("This is content of JSON file: {0}".format(file))


get_gz()
if arguments.download:
    if not exists:
        get_zip()
    else:
        print("File exists.")


if arguments.format == 'json':
    with open('movies.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
    with open('json_format.json', 'w') as csv_file:
        json.dump(rows, csv_file)
    print("Json created.")


if arguments.format == 'xml':
    with open('movies.csv') as csv_file:
        text = csv_file.readlines()
    root = ET.Element('root')
    root.text = str(text)
    tree = ET.ElementTree(root)
    tree.write('xml-format.xml')
    print("Xml created.")


if arguments.format == 'csv':
    with open('movies.csv') as csv_file:
        csvreader = csv.reader(csv_file)
        text = []
        for row in csvreader:
            text += row
    with open('csv-format.csv', 'w') as csv_f:
        csv_writer = csv.writer(csv_f)
        csv_writer.writerow(text)
    print("Csv created.")


if arguments.format == 'yaml':
    with open('movies.csv') as csv_f:
        csvreader = csv.reader(csv_f)
        text = []
        for row in csvreader:
            text += row
    with open('yaml-format.yaml', 'w') as f:
        yaml.dump(text, csv_file, default_flow_style=False)
    print('yaml created.')
