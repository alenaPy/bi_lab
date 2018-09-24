"""Exittask."""
import argparse
from collections import OrderedDict
import csv
import io
import json
import os
import requests
import yaml
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--year', help='displays Top250 movies titles with year',
                    action="store_true")
parser.add_argument('--rate', help='displays Top250 movies titles with rate',
                    action="store_true")
parser.add_argument('--all', help='shows title, rate, year',
                    action="store_true")
parser.add_argument('--histogram', help='displays histogram for rating or for'
                    ' years (in text format)', default=False)
parser.add_argument('--output', help='stores all data to specified filename'
                    ' file', default=False)
parser.add_argument('--format', default=False)
arguments = parser.parse_args()

s = 'New  Distribution  Votes  Rank  Title'
dataStart = 0
counter = 0
f = 'ratings.list'
movies = []
try:
    with open(f, 'r') as fp:
        for line in fp:
            if s in line:
                dataStart = 1
            elif dataStart == 1 and len((line.strip())) != 0:
                rate = line.strip().split('  ')[2]
                b = line.strip().split('  ')[3]
                c = b.split(' (')
                name = c[0]
                year = c[1][0:4:1]
                movies.append([name, year, rate])
                counter += 1
                if (arguments.year is False and arguments.rate is False and
                        arguments.histogram is False and
                        arguments.all is False and arguments.output is False and
                        arguments.format is False):
                    print(name)
            if counter == 250:
                break
except FileNotFoundError:
    print('File not found')
    exit()

years = []
for movie in range(250):
    years.append(movies[movie][1])
d_years = dict((i, years.count(i)) for i in years)
r = []
for movie in range(250):
    r.append(movies[movie][2])
d_rate = dict((i, r.count(i)) for i in r)

# Check arguments
if arguments.year:
    print('Top250 movies titles with year')
    i = 0
    for movie in movies:
        i += 1
        print((str(i) + '. ' + movie[0] + ' ' + movie[1]))

if arguments.rate:
    print('Top250 movies titles with rate')
    i = 0
    for movie in movies:
        i += 1
        print((str(i) + '. ' + movie[0] + ' ' + movie[2]))

if arguments.histogram == 'rate':
    print('Rate histogram.')
    for movie in d_rate:
        print(str(movie) + ' ' + '*' * d_rate[movie] + ' ' +
              str(d_rate[movie]))

elif arguments.histogram == 'year':
    print('Year histogram.')
    for movie in d_years:
        print(str(movie) + ' ' + '*' * d_years[movie] + ' ' +
              str(d_years[movie]))

if arguments.all:
    print('Top250 movies. Title, rate, year')
    i = 0
    for movie in movies:
        i += 1
        print((str(i) + '. ' + movie[0] + ' ' + movie[2] + ' ' + movie[1]))

if arguments.output:
    print('Write to ' + arguments.output)
    out_file = open(arguments.output, "w")
    i = 0
    for movie in movies:
        i += 1
        out_file.write((str(i) + '. ' + movie[0] + ' ' + movie[2] + ' ' +
                        movie[1]) + '\n')
    out_file.close()

csv_file = 'table.csv'

# zip file
exists = os.path.isfile(csv_file)
if not exists:
    try:
        zip_url = 'https://github.com/natalliahaisionak/Files/raw/master/6.zip'
        zip_get = requests.get(zip_url)
        data = zipfile.ZipFile(io.BytesIO(zip_get.content))
        data.extractall()
        data.close()
        print('zip archive extracted')
    except zipfile.BadZipfile:
        print('BadZipfile: File is not a zip file')
else:
    print('data file ' + csv_file + ' exists')

# to csv
if arguments.format == 'csv':
    with open(csv_file) as file:
        csv_rd = csv.reader(file)
        with open('csv_output.csv', 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            for row in csv_rd:
                writer.writerow(row)


# to JSON
if arguments.format == 'json':
    fieldnames = (
        "SERVICE_STATION", "ADDR", "POST", "STREET", "BUILDING", "CITY_ID",
        "CITY",
        "COUNTRY", "CODE")
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

# to yaml
if arguments.format == 'yaml':
    in_file = open(csv_file, "r")
    out_file = open('yaml_file.yaml', "w")
    items = []

    def convert_to_yaml(line):
        """Convert to yaml."""
        item = {
            'SERVICE_STATION': line[0],
            'ADDR': line[1],
            'POST': line[2],
            'STREET': line[3],
            'BUILDING': line[4],
            'CITY_ID': line[5],
            'CITY': line[6],
            'COUNTRY': line[7],
            'CODE': line[8]
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
