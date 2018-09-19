titles = []
rates = []
years = []

try:
    with open('ratings.list', 'r', encoding='ISO-8859-1') as readFile:
        for i, line in enumerate(readFile):
            if i >= 28 and i < 278:
                titles.append(line[:line.find('(')].split('  ')[6])
                rates.append(line.split('  ')[5])
                years.append(line[line.find('(') + 1:line.find(')')])


except FileNotFoundError:
    print('Error. File isn''t find! \n')


with open('titles.txt', 'w', encoding='UTF-8') as titlesFile:
    for x in titles:
        titlesFile.write(x + '\n')


with open('rates.txt', 'w', encoding='UTF-8') as ratesFile:
    dictionary_1 = dict((x, rates.count(x)) for x in set(rates))
    for x in dictionary_1:
        ratesFile.write(str(x) + ' ' + '*' * dictionary_1[x] + ' ' + str(dictionary_1[x]) + '\n')


with open('years.txt', 'w', encoding='UTF-8') as yearsFile:
    dictionary_2 = dict((x, years.count(x)) for x in set(years))
    for x in dictionary_2:
        yearsFile.write(str(x) + ' ' + '*' * dictionary_2[x] + ' ' + str(dictionary_2[x]) + '\n')
