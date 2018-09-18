"""Read and save data practice."""

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
                film.append(line.strip().rstrip(')').split('  ')[3].
                            split(' (')[0])
                year.append(line.strip().rstrip('/I)').split('  ')[3].
                            split(' (')[1])
                i += 1
except FileNotFoundError:
    print('The file hasn\'t been found')

rank = dict(zip(rank, list(map(lambda x: rank.count(x), rank))))
year = dict(zip(year, list(map(lambda x: year.count(x), year))))
top250_movies = open('top250_movies.txt', 'w', encoding='UTF-8')
ratings = open('ratings.txt', 'w', encoding='UTF-8')
years = open('years.txt', 'w', encoding='UTF-8')


for obj in film:
    top250_movies.write(obj + '\n')
for key in rank:
    ratings.write(key + ' ' + str(rank[key]) + '\n')
for key in year:
    years.write(key + ' ' + str(year[key]) + '\n')

top250_movies.close()
ratings.close()
years.close()
