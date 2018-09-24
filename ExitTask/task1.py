"""Exit task."""

import argparse
import csv
import json
import os
import urllib.request
import xml.etree.cElementTree as ET
import yaml
import zipfile

movies, rates, years, r, = [], [], [], []

parser = argparse.ArgumentParser()

parser.add_argument("--year", help="displays Top250 movies titles with year",
                    action="store_true")
parser.add_argument("--rate", help="displays Top250 movies titles with rate",
                    action="store_true")
parser.add_argument("--all", help="shows title, rate, year",
                    action="store_true")
parser.add_argument("--histogram",
                    help="displays histogram for /"
                         " rating or for years (in text format)")
parser.add_argument("--output",
                    help="stores all data to specified filename file")
parser.add_argument("--download", help="Provide downloading of files",
                    action="store_true")
parser.add_argument("--format",
                    help='Use json | xml | csv | yaml'
                    ' to convert to choosen format')

arguments = parser.parse_args()

exists = os.path.isfile('ratings.zip')


def get_zip():
    """Download zip archive."""
    urllib.request.urlretrieve(
        'https://github.com/ZhenyaBond/bi_lab/raw/master/ratings.zip',
        'ratings.zip')
    print("Downloaded successfully.")


def read_zip():
    """Read all content of zip."""
    zip_f = zipfile.ZipFile('ratings.zip')
    zip_f.extractall()
    zip_f.close()

    try:
        cnt = 0
        with open("ratings.list", 'r', encoding='iso-8859-1') as imdb:
            for line in imdb:
                if "New  Distribution  Votes  Rank  Title" in line:
                    break
            for line in imdb:
                if cnt < 250:
                    title = line.strip().split('  ')[3].split('(')[0]\
                        .strip()
                    year = line[line.find('(') + 1:line.find(')')]\
                        .rstrip('/I)')
                    rate = line.strip().split('  ')[2]\
                        .strip()
                    movies.append([title, year, rate])
                cnt += 1

    except FileNotFoundError:
        print('File not found!')


if arguments.year is False and\
        arguments.rate is False and\
        arguments.histogram is False and\
        arguments.all is False and\
        arguments.output is False and\
        arguments.download is False and\
        arguments.format is False:
    read_zip()
    i = 0
    for movie in movies:
        i += 1
        print(str(i) + '. ' + movie[0])

if arguments.year:
    print('Top250 movies titles with year')
    read_zip()
    i = 0
    for movie in movies:
        i += 1
        print((str(i) + '. ' + movie[0] + ' ' + movie[1]))

if arguments.rate:
    print('Top250 movies titles with rate')
    read_zip()
    i = 0
    for movie in movies:
        i += 1
        print((str(i) + '. ' + movie[0] + ' ' + movie[2]))


if arguments.histogram == 'rate':
    print('Rate histogram.')
    read_zip()
    for movie in range(250):
        r.append(movies[movie][2])
    d_rate = dict((i, r.count(i)) for i in r)

    for movie in d_rate:
        print(str(movie) + ' ' + '*' * d_rate[movie] + ' ' +
              str(d_rate[movie]))


if arguments.histogram == 'year':
    print('Year histogram.')
    read_zip()
    years = []
    for movie in range(250):
        years.append(movies[movie][1])
    d_years = dict((i, years.count(i)) for i in years)

    for movie in d_years:
        print(str(movie) + ' ' + '*' * d_years[movie] + ' ' +
              str(d_years[movie]))


if arguments.all:
    print('Top250 movies. Title, rate, year')
    read_zip()
    i = 0
    for movie in movies:
        i += 1
        print((str(i) + '. ' + movie[0] + ' ' + movie[2] + ' ' + movie[1]))


if arguments.output:
    read_zip()
    out_file = open(arguments.output, "w", encoding='iso-8859-1')
    i = 0
    for movie in movies:
        i += 1
        out_file.write((str(i) + '. ' + movie[0] + ' ' + movie[2] + ' ' +
                        movie[1]) + '\n')
    out_file.close()

if arguments.download:
    if not exists:
        get_zip()
    else:
        print("File exists.")

if arguments.format == 'json':
    read_zip()
    with open('json_format.json', 'w', encoding='iso-8859-1') as f:
        json.dump(movies, f)
    f.close()
    print("json created.")

if arguments.format == 'xml':
    read_zip()
    root = ET.Element('root')
    root.text = str(movies)
    tree = ET.ElementTree(root)
    tree.write('xml-format.xml')
    print("xml-created.")

if arguments.format == 'csv':
    read_zip()
    with open('csv-format.csv', 'w', encoding='iso-8859-1') as csv_f:
        csv_writer = csv.writer(csv_f)
        csv_writer.writerow(movies)
    csv_f.close()
    print("csv created.")

if arguments.format == 'yaml':
    read_zip()
    with open('yaml-format.yaml', 'w', encoding='iso-8859-1') as f:
        yaml.dump(movies, f, default_flow_style=False)
    f.close()
    print('yaml created.')
