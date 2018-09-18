"""Read and save data practice."""

titles = []
rates = []
years = []


try:
    with open('ratings.list', 'r', encoding='ISO-8859-1') as dbdata:
        for i, line in enumerate(dbdata):

            if i >= 28 and i < 278:

                titles.append(line[:line.find('(')].split('  ')[6])
                rates.append(line.split('  ')[5])
                years.append(line[line.find('(') + 1:line.find(')')])

except FileNotFoundError:
    print('This file is not found! \n')


with open('titles.txt', 'w', encoding='UTF-8') as ttl:
    for x in titles:
        ttl.write(x + '\n')

with open('rates.txt', 'w', encoding='UTF-8') as rts:

    dict1 = dict((x, rates.count(x)) for x in set(rates))
    for x in dict1:
        rts.write(x + ' ' + str(dict1[x]) + '\n')

with open('years.txt', 'w', encoding='UTF-8') as yrs:

    dict2 = dict((x, years.count(x)) for x in set(years))

    for x in dict2:
        yrs.write(x + ' ' + str(dict2[x]) + '\n')
