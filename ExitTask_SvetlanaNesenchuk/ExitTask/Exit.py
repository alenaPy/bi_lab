"""Exit Task."""


import argparse
from collections import OrderedDict
import csv
import io
import json
import os
import requests
import yaml
import zipfile


# Parse file with IMDB ratings.
titles = []
years = []
ratings = []
try:
    count = 0
    with open('ratings.list', 'r', encoding='ISO-8859-1') as file:
        for line in file:
            if 'New  Distribution  Votes  Rank  Title' in line:
                break
        for line in file:
            if count < 250:
                # replace('(', ' ') implemented with the aim to facilitate
                # split movie title from its year
                movie = line.strip().replace('(', ' ').split('  ')
                titles.append(movie[3])
                years.append(movie[4].rstrip('/I)'))
                ratings.append(movie[2].lstrip())
                count += 1
except FileNotFoundError:
    print("This file doesn't exist")

# Create dictionaries with frequencies of years and ratings.

year_frequency = {year: years.count(year) for year in years}
rating_frequency = {rating: ratings.count(rating) for rating in ratings}

# Put result in separate .txt files.

with open('titles.txt', 'w', encoding='UTF-8') as titles_file:
    for item in titles:
        titles_file.write(item + '\n')
with open('years.txt', 'w', encoding='UTF-8') as years_file:
    for key in sorted(year_frequency):
        # Histogram is created in the way of representing number of films
        # for certain year by according number of pluses.
        years_file.write(key + ': ' + '+' * year_frequency[key] +
                         ' ' + str(year_frequency[key]) + '\n')
with open('ratings.txt', 'w', encoding='UTF-8') as ratings_file:
    for key in sorted(rating_frequency):

        # Histogram is created in the way of representing number of films

        # for certain rank by according number of pluses.

        ratings_file.write(key + ': ' + '+' * rating_frequency[key] +

                           ' ' + str(rating_frequency[key]) + '\n')

# Parsing arguments entered from the command line.

parser = argparse.ArgumentParser(description='Choose option for IMDB '
                                             'Top250 show.', add_help=True)
parser.add_argument('--year', action='store_true',
                    help='displays Top250 movies titles with year')
parser.add_argument('--rate', action='store_true',
                    help='displays Top250 movies titles with rate')
parser.add_argument('--all', action='store_true',
                    help='shows title, rate, year')
parser.add_argument('--histogram',
                    help='displays histogram for rating or for years')
parser.add_argument('--output',
                    help='stores all data to specified filename file')
parser.add_argument('--format',
                    help='stores all data in the specified format')
arguments = parser.parse_args()
if arguments.year:
    print('----------Title---------------Year---\n')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + years[i] + '\n')
elif arguments.rate:
    print('----------Title---------------Rate----')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + ratings[i] + '\n')
elif arguments.all:
    print('----------Title---------------Rate--Year--')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + ratings[i] +
              ' - ' + years[i] + '\n')
elif arguments.histogram == 'rating':
    print('Histogram for quantity of films for each rating')
    for key in sorted(rating_frequency):
        print(key + ': ' + '+' * rating_frequency[key] +
              ' ' + str(rating_frequency[key]) + '\n')
elif arguments.histogram == 'year':
    print('Histogram for quantity of films for each year')
    for key in sorted(year_frequency):
        print(key + ': ' + '+' * year_frequency[key] +
              ' ' + str(year_frequency[key]) + '\n')
elif arguments.format == 'json':
    fieldnames = ("CAR_ID", "MODEL", "MANUFACTURE_YEAR", "FUEL_TYPE",
                  "ENGINE_DISPLACEMENT", "ENGINE_POWER")
    entries = []
    with open('cars.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames)
        for row in reader:
            entry = OrderedDict()
            for field in fieldnames:
                entry[field] = row[field]
            entries.append(entry)
        output = {"Cars": entries}
        with open('file.json', 'w') as jsonfile:
            json.dump(output, jsonfile)
            jsonfile.write('\n')
elif arguments.format == 'xml':
    csvData = csv.reader(open('cars.csv'))
    xmlData = open('carsXML.xml', 'w')
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
elif arguments.format == 'yaml':
    in_file = open('cars.csv', "r")
    out_file = open('yaml_file.yaml', "w")
    items = []

    def convert_to_yaml(line):
        """Convert to yaml."""
        item = {
            'CAR_ID': line[0],
            'MODEL': line[1],
            'MANUFACTURE_YEAR': line[2],
            'FUEL_TYPE': line[3],
            'ENGINE_DISPLACEMENT': line[4],
            'ENGINE_POWER': line[5]
        }
        items.append(item)
    try:
        reader = csv.reader(open('cars.csv', "r"))
        # skip headers
        next(reader)
        for i, line in enumerate(reader):
            convert_to_yaml(line)
        out_file.write(yaml.dump(items, default_flow_style=False))
    finally:
        in_file.close()
        out_file.close()
# to csv
elif arguments.format == 'csv':
    with open('cars.csv') as file:
        csv_rd = csv.reader(file)
        with open('csv_output.csv', 'w', newline='') as write_file:
            writer = csv.writer(write_file)
            for row in csv_rd:
                writer.writerow(row)
                print(', '.join(row))
elif arguments.output:
    with open(arguments.output + '.txt', 'w', encoding='UTF-8') as file:
        for i, value in enumerate(titles):
            file.write(str(i + 1) + '. ' + titles[i] + ' - ' +
                       ratings[i] + ' - ' + years[i] + '\n')
    print('Data was successfully written to the file.')
else:
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + '\n')

# Download zip.
file = 'FL_insurance_sample.csv'
exists = os.path.isfile(file)
if not exists:
    try:
        zip_url = 'http://spatialkeydocs.s3.amazonaws.com/' \
                  'FL_insurance_sample.csv.zip'
        zip_get = requests.get(zip_url)
        data = zipfile.ZipFile(io.BytesIO(zip_get.content))
        data.extractall()
        data.close()
        print('zip archive extracted')
    except zipfile.BadZipfile:
        print('BadZipfile: File is not a zip file')
else:
    print('data file ' + file + ' exists')
