"""Arguments processing."""

import argparse
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
                movie = line.strip().replace('(', ' ').split('  ')
                titles.append(movie[3])
                years.append(movie[4].rstrip('/I)'))
                ratings.append(movie[2].lstrip())
                count += 1
except FileNotFoundError:
    print("This file doesn't exist")

year_count = {year: years.count(year) for year in years}
rating_count = {rating: ratings.count(rating) for rating in ratings}

parser = argparse.ArgumentParser()
parser.add_argument('--year', help='displays Top250 movies titles with year',
                    default=False)
parser.add_argument('--rate', help='displays Top250 movies titles with rate',
                    default=False)
parser.add_argument('--all', help='shows title, rate, year', default=False)
parser.\
    add_argument('--histogram', help='displays histogram for rating '
                 'or for years (in text format)', default=False)
parser.add_argument('--output', help='stores all data to specified filename'
                                     ' file', default=False)
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
        print(str(i + 1) + '. ' + titles[i] + ' - ' +
              ratings[i] + ' - ' + years[i] + '\n')

elif arguments.histogram == 'rating':
    print('Histogram for quantity of films for each rating')
    for key in sorted(rating_count):
        print(key + ': ' + '+' * rating_count[key] +
              ' ' + str(rating_count[key]) + '\n')

elif arguments.histogram == 'year':
    print('Histogram for quantity of films for each year')
    for key in sorted(year_count):
        print(key + ': ' + '+' * year_count[key] +
              ' ' + str(year_count[key]) + '\n')
else:
    with open(arguments.output + '.txt', 'w', encoding='UTF-8') as file:
        for i, value in enumerate(titles):
            file.write(str(i + 1) + '. ' + titles[i] + ' - ' +
                       ratings[i] + ' - ' + years[i] + '\n')
    print('Data was successfully written to the file.')
