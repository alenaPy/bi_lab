import argparse

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

except FileNotFoundError:
    print('This file is not found! \n')


dict1 = dict((x, rates.count(x)) for x in set(rates))  # dictionary with rates
dict2 = dict((x, years.count(x)) for x in set(years))  # dictionary with years


# Check arguments
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

if arguments.histogram == 'rate':
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
