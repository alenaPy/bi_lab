"""Creating three txt files."""
movies = []
try:
    count = 0
    with open('ratings.list', 'r', encoding='ISO-8859-1') as file:
        for line in file:
            if 'New  Distribution  Votes  Rank  Title' in line:
                break
        for line in file:
            if count < 250:
                movies0 = line.strip().split('  ')
                movies.append([movies0[2].lstrip(), movies0[3].rstrip(')').rstrip('/I').split('(')])
                count += 1
except FileNotFoundError:
    print("This file doesn't exist")
years = []
ratings = []
for item in movies:
    years.append(item[1][1])
    ratings.append(item[0])
year_count = {year: years.count(year) for year in years}
rating_count = {rating: ratings.count(rating) for rating in ratings}
with open('titles.txt', 'w', encoding='UTF-8') as titles_file:
    for item in movies:
        titles_file.write(item[1][0] + '\n')
with open('years.txt', 'w', encoding='UTF-8') as years_file:
    for key, val in year_count.items():
        years_file.write(key + ': ' + str(val) + '\n')
with open('ratings.txt', 'w', encoding='UTF-8') as ratings_file:
    for key, val in rating_count.items():
        ratings_file.write(key + ': ' + str(val) + '\n')
