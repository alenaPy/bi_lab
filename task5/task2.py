"""Task5."""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--year", help="displays Top250 movies titles with year")
parser.add_argument("--rate", help="displays Top250 movies titles with rate")
parser.add_argument("--all", help="shows title, rate, year")
parser.add_argument("--histogram",
                    help="displays histogram for /"
                         " rating or for years (in text format)")
parser.add_argument("--output",
                    help="stores all data to specified filename file")

arguments = parser.parse_args()


def count_(lst):
    """Return a dictionary with element count in a given list."""
    dic = {}
    for x in range(len(lst)):
        cntt = 0
        for y in range(len(lst)):
            if lst[x] == lst[y]:
                cntt += 1
        dic[lst[x]] = cntt
    return dic


movies = []

try:
    cnt = 0
    with open("ratings.list", 'r', encoding='iso-8859-1') as imdb:
        for line in imdb:
            if "New  Distribution  Votes  Rank  Title" in line:
                break
        for line in imdb:
            if cnt < 250:
                title = line.strip().split('  ')[3].split('(')[0].strip()
                year = line[line.find('(') + 1:line.find(')')].rstrip('/I)')
                rate = line.strip().split('  ')[2].strip()
                movies.append([title, year, rate])
            cnt += 1

except FileNotFoundError:
    print('File not found!')


years = []
for movie in range(250):
    years.append(movies[movie][1])
d_years = dict((i, years.count(i)) for i in years)

r = []
for movie in range(250):
    r.append(movies[movie][2])

d_rate = dict((i, r.count(i)) for i in r)


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
    out_file = open(arguments.output, "w")
    i = 0
    for movie in movies:
        i += 1
        out_file.write((str(i) + '. ' + movie[0] + ' ' + movie[2] + ' ' +
                        movie[1]) + '\n')
    out_file.close()
