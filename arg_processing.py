"""Labwork5 Natallia Haisionak."""
import argparse

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
