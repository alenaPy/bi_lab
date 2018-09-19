"""Task4."""


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


try:
    cnt = 0
    movies, rates, years = [], [], []
    with open("ratings.list", 'r', encoding='iso-8859-1') as imdb:
        for line in imdb:
            if "New  Distribution  Votes  Rank  Title" in line:
                break
        for line in imdb:
            if cnt < 250:
                title = line.strip().split('  ')[3].split('(')[0].strip()
                year = line[line.find('(') + 1:line.find(')')].rstrip('/I)')
                rate = line.strip().split('  ')[2].strip()
                movies.append(title)
                rates.append(rate)
                years.append(year)
                cnt += 1

    rates = dict(count_(rates))
    years = dict(count_(years))

    titles = open("top250_movies.txt", "w", encoding='iso-8859-1')
    titles.write('\n'.join(movies))

    ratings = open("ratings.txt", "w", encoding='iso-8859-1')
    for i in sorted(rates):
        ratings.write(i + ' ' + '*' * rates[i] + '\n')

    years_ = open("years.txt", "w", encoding='iso-8859-1')
    for i in sorted(years):
        years_.write(i + ' ' + '*' * years[i] + '\n')

except FileNotFoundError:
    print('File not found!')
