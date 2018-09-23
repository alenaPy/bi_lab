"""Read and save data practice."""

import argparse

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('--year', default=False, action='store_true',
                    help='displays Top250 movies titles with year')
parser.add_argument('--rate', default=False, action='store_true',
                    help='displays Top250 movies titles with rate')
parser.add_argument('--all', default=False, action='store_true',
                    help='shows title, rate, year')
parser.add_argument('--histogram', default=False,
                    help='displays histogram for rating or '
                         'for years (in text format)')
parser.add_argument('--output', default=False,
                    help='stores all data to specified filename file')

args = parser.parse_args()

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

hist_rank = dict(zip(rank, list(map(lambda x: rank.count(x), rank))))
hist_year = dict(zip(year, list(map(lambda x: year.count(x), year))))


if args.year:
    for i in range(len(film)):
        print(i + 1, '. ', film[i], ' (', year[i], ')\n')
if args.rate:
    for i in range(len(film)):
        print(i + 1, '. ', film[i], ' ', rank[i], '\n')
if args.all:
    for i in range(len(film)):
        print(i + 1, '. ', film[i], ' (', year[i], ') ', rank[i], '\n')
if args.histogram == 'rating':
    for key in hist_rank:
        print(key + ' ' + hist_rank[key] * '*' + '\n')
if args.histogram == 'year':
    for key in hist_year:
        print(key + ' ' + hist_year[key] * '*' + '\n')
if args.output:
    with open(args.output, 'w', encoding='UTF-8') as file:
        for i in range(len(film)):
            file.write(str(i + 1) + '. ' + film[i] + ' (' + str(year[i]) +
                       ') ' + str(rank[i]) + '\n')
