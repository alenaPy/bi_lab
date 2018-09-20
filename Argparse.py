"""ArgumentsProcessing."""


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--year', help='displays Top250 movie titles with year',
                    action='store_true')
parser.add_argument('--rate', help='displays Top250 movie titles with rate',
                    action='store_true')
parser.add_argument('--all', help='shows title, rate, year', action='store_true')
parser.add_argument('--histogram', help='displays histogram for rating or for'
                    ' years (in text format)')
parser.add_argument('--output', help='stores all data to specified filename'
                    ' file')

arguments = parser.parse_args()
list1 = []
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
                list1.append([title, rat, year])
except FileNotFoundError:
    print('Not exists')

year = []
for y in range(250):
    year.append(list1[y][2])
dict_year = dict((i, year.count(i)) for i in year)
print(year)

rating = []
for y in range(250):
    rating.append(list1[y][1])
dict_rat = dict((i, rating.count(i)) for i in rating)
print(rating)


if arguments.year:
    print('Top250 movies titles with year')
    i = 0
    for y in list1:
        i += 1
        print((str(i) + '. ' + y[0] + ' ' + y[1]))
if arguments.rate:
    print('Top250 movies titles with rate')
    i = 0
    for y in list1:
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
    for y in list1:
        i += 1
        print((str(i) + '. ' + y[0] + ' ' + y[2] + ' ' + y[1]))
if arguments.output:
    print(arguments.output)
    out_file = open(arguments.output, "w")
    i = 0
    for y in list1:
        i += 1
        out_file.write((str(i) + '. ' + y[0] + ' ' + y[2] + ' ' +
                        y[1]) + '\n')
    out_file.close()
