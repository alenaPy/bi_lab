"""Solution for work with IMDB rankings."""
import argparse
import csv
import dicttoxml
import json
import os
import sys
import urllib.request
import yaml


def download_file(url='http://pilomaterialy-timber.com/'
                      'wp-content/uploads/'
                      '2012/09/rake-reyki-sosna-brusok-'
                      'price-list-Sunrise-Ltd-Kiev.pdf'):
    """Download file with input URL."""
    file_name = url.split('/')[-1]
    file_path = 'D:\Artsiom_Barysionak\Python\ExitTask\\' + file_name
    if not os.path.isfile(file_path):
        try:
            urllib.request.urlretrieve(url, file_path)
            print('%s file nas been successfully downloaded.' % file_name)
        except Exception:
            print('File has not been downloaded. An error occured.')
            parser.print_help()
    else:
        print('%s has been already downloaded.' % file_name)


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

# Put all results for certain movie in th dictionary.
movies_list = []
for i in range(len(titles)):
    movies_list.append({'Title': titles[i], 'Year': years[i],
                        'Rank': ratings[i]})
content = {'IMDB Top250 Movies': movies_list}

# Parsing arguments entered from the command line.
parser = argparse.ArgumentParser(description='Choose option for IMDB '
                                             'Top250 show.', add_help=True)
parser.add_argument('--year', action='store_true',
                    help='displays Top250 movies titles with year')
parser.add_argument('--rate', action='store_true',
                    help='displays Top250 movies titles with rate')
parser.add_argument('--all', action='store_true',
                    help='shows title, rate, year')
parser.\
    add_argument('--download', type=str, nargs='?', const=1,
                 help='specify file URL or nothing to download default file')
parser.add_argument('--histogram',
                    help='displays histogram for rating or for years')
parser.add_argument('--format', type=str,
                    help='specify what format convert data to')
parser.add_argument('--output',
                    help='stores all data to specified filename file')
arguments = parser.parse_args()
# Default action (if no arguments were set).
if len(sys.argv) == 1:
    for item in titles:
        print(item)

if arguments.year:
    print('----------Title---------------Year---\n')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + years[i] + '\n')

if arguments.rate:
    print('----------Title---------------Rate----')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + ratings[i] + '\n')

if arguments.all:
    print('----------Title---------------Rate--Year--')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + ratings[i] +
              ' - ' + years[i] + '\n')

if arguments.download:
    if arguments.download == 1:
        download_file()
    else:
        download_file(arguments.download)

if arguments.histogram == 'rating':
    print('Histogram for quantity of films for each rating')
    for key in sorted(rating_frequency):
        print(key + ': ' + '+' * rating_frequency[key] +
              ' ' + str(rating_frequency[key]) + '\n')
if arguments.histogram == 'year':
    print('Histogram for quantity of films for each year')
    for key in sorted(year_frequency):
        print(key + ': ' + '+' * year_frequency[key] +
              ' ' + str(year_frequency[key]) + '\n')

if arguments.format == 'json':
    with open('data.json', 'w', encoding='UTF-8') as json_output:
        json.dump(content, json_output)
    print('Data has been successfully loaded into json file.')
if arguments.format == 'xml':
    xml_content = dicttoxml.dicttoxml(content, attr_type=False)
    with open('data.xml', 'wb', encoding='UTF-8') as xml_output:
        xml_output.write(xml_content)
    print('Data has been successfully loaded into xml file.')
if arguments.format == 'csv':
    with open('data.csv', 'w', encoding='UTF-8') as csv_output:
        csv_writer = csv.writer(csv_output, delimiter=' ')
        for item in movies_list:
            for value in item.values():
                csv_writer.writerow(value)
    print('Data has been successfully loaded into csv file.')
if arguments.format == 'yaml':
    with open('data.yaml', 'w') as yaml_output:
        yaml.dump(content, yaml_output, default_flow_style=False)
    print('Data has been successfully loaded into yaml file.')

if arguments.output:
    with open(arguments.output, 'w', encoding='UTF-8') as file_output:
        file_output.write(str(content))
