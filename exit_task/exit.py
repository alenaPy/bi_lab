import argparse
from collections import OrderedDict
import csv
import gzip
import io
import json
import os
import requests
import yaml
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('--year', action="store_true",
                    help='Top250 movies titles with year',
                    default=False)
parser.add_argument('--rate', action="store_true",
                    help='Top250 movies titles with rate',
                    default=False)
parser.add_argument('--all', action="store_true",
                    help='Prints title, rate, year',
                    default=False)
parser.add_argument('--histogram', help='Prints histogram for rating or for'
                                        ' years (in text format)',
                    default=False)
parser.add_argument('--output', help='stores all data to specified '
                                     'filename file',
                    default=False)
parser.add_argument('--titles', action="store_true",
                    help='Top250 movies titles',
                    default=False)
parser.add_argument('--download [url]', action="store_true",
                    help='Download file from URL',
                    default=False)
parser.add_argument('--format', default=False)

arguments = parser.parse_args()
titles = []
rates = []
years = []
films = []

try:
    with open('ratings.list', 'r', encoding='ISO-8859-1') as dbdata:
        for i, line in enumerate(dbdata):
            if i >= 28 and i < 278:
                films.append([line[:line.find('(')].split('  ')[6],
                              line[line.find('(') + 1:line.find(')')],
                              line.split('  ')[5]])
                titles.append(line[:line.find('(')].split('  ')[6])
                rates.append(line.split('  ')[5])
                years.append(line[line.find('(') + 1:line.find(')')])

        if (arguments.year is False and arguments.rate is False and
            arguments.histogram is False and arguments.all is False and
            arguments.output is False and arguments.format is False):
            arguments.titles = True

except FileNotFoundError:
    print('This file is not found! \n')

dict1 = dict((x, rates.count(x)) for x in set(rates))  # dictionary with rates
dict2 = dict((x, years.count(x)) for x in set(years))  # dictionary with years
csv_file = 'programs.csv'

# zip file
exists = os.path.isfile(csv_file)
if not exists:
    zip_url = 'https://github.com/SimonenkoV/bi_lab/raw/Exit_Task/exit_task/programs.zip'
    zip_get = requests.get(zip_url)
    data = zipfile.ZipFile(io.BytesIO(zip_get.content))
    data.extractall()
    data.close()
    print('zip archive extracted')
else:
    print('data file ' + csv_file + ' already exists')


# Check arguments

# to csv
if arguments.format == 'csv':
    with open(csv_file) as file:
        csv_rd = csv.reader(file)
        with open('csv_output.csv', 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            for row in csv_rd:
                writer.writerow(row)
                print(', '.join(row))


# to JSON
if arguments.format == 'json':
    fieldnames = (
        "CATEGORY_CODE", "CATEGORY_NAME", "PROGRAM_CODE", "COMMODITY_CODE",
        "COMMODITY_NAME", "PROGRAM_NAME")
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


# to yaml
if arguments.format == 'yaml':
    in_file = open(csv_file, "r")
    out_file = open('yaml_file.yaml', "w")
    items = []
    def convert_to_yaml(line):
        """Convert to yaml."""
        item = {
            'CATEGORY_CODE': line[0],
            'CATEGORY_NAME': line[1],
            'PROGRAM_CODE': line[2],
            'COMMODITY_CODE': line[3],
            'COMMODITY_NAME': line[4],
            'PROGRAM_NAME': line[5],
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

# print
if arguments.titles:
    print('Top250 movies titles')
    i = 0
    for i in range(0, len(titles), 1):
        print(str(i + 1) + ' ' + titles[i])
        i += 1

if arguments.year:
    print('Top250 movies titles with year')
    i = 0
    for i in range(0, len(titles), 1):
        print(str(i + 1) + ' ' + titles[i] + ' ' + years[i])
        i += 1

if arguments.rate:
    print('Top250 movies titles with rate')
    i = 0
    for i in range(0, len(titles)):
        print(str(i + 1) + ' ' + titles[i] + ' ' + rates[i])
        i += 1
if arguments.histogram == 'rating':
    print('Rate histogram.')
    for x in dict1:
        print(str(x) + ' ' + '*' * dict1[x] + ' ' + str(dict1[x]))


elif arguments.histogram == 'year':
    print('Year histogram.')
    for x in dict2:
        print(str(x) + ' ' + '*' * dict2[x] + ' ' + str(dict2[x]))

if arguments.all:
    print('Top250 movies. Title, rate, year')
    i = 0
    for i in range(0, len(titles), 1):
        print(str(i + 1) + '. ' + titles[i] + ' ' + years[i] + ' ' + rates[i])
        i += 1

if arguments.output:
    print('Write to ' + arguments.output)
    with open(arguments.output, "w", encoding='UTF-8') as file1:
        i = 0
        for i in range(0, len(titles)):
            file1.write((str(i + 1) + '. ' + titles[i] + ' ' + years[i] + ' ' +
                         rates[i]) + '\n')
            i += 1
