"""Parse file with IMDB ratings and put result in separate .txt files."""
import argparse

# Parse file with IMDB ratings.
titles = []
years = []
ratings = []
try:
    count = 0
    with open('ratings.list', 'r', encoding='ISO-8859-1') as file:
        for line in file:
            if 'New  Distribution  Votes  Rank  Title' in line:
                break
        for line in file:
            if count < 250:
                # replace('(', ' ') implemented with the aim to facilitate
                # split movie title from its year
                movie = line.strip().replace('(', ' ').split('  ')
                titles.append(movie[3])
                years.append(movie[4].rstrip('/I)'))
                ratings.append(movie[2].lstrip())
                count += 1
except FileNotFoundError:
    print("This file doesn't exist")

# Create dictionaries with frequencies of years and ratings.

year_frequency = {year: years.count(year) for year in years}
rating_frequency = {rating: ratings.count(rating) for rating in ratings}

# Put result in separate .txt files.
with open('titles.txt', 'w', encoding='UTF-8') as titles_file:
    for item in titles:
        titles_file.write(item + '\n')
with open('years.txt', 'w', encoding='UTF-8') as years_file:
    for key in sorted(year_frequency):
        # Histogram is created in the way of representing number of films
        # for certain year by according number of pluses.
        years_file.write(key + ': ' + '+' * year_frequency[key] +
                         ' ' + str(year_frequency[key]) + '\n')
with open('ratings.txt', 'w', encoding='UTF-8') as ratings_file:
    for key in sorted(rating_frequency):
        # Histogram is created in the way of representing number of films
        # for certain rank by according number of pluses.
        ratings_file.write(key + ': ' + '+' * rating_frequency[key] +
                           ' ' + str(rating_frequency[key]) + '\n')

# Parsing arguments entered from the command line.
parser = argparse.ArgumentParser(description='Choose option for IMDB '
                                             'Top250 show.', add_help=True)
parser.add_argument('--year', action='store_true',
                    help='displays Top250 movies titles with year')
parser.add_argument('--rate', action='store_true',
                    help='displays Top250 movies titles with rate')
parser.add_argument('--all', action='store_true',
                    help='shows title, rate, year')
parser.add_argument('--histogram',
                    help='displays histogram for rating or for years')
parser.add_argument('--output',
                    help='stores all data to specified filename file')
arguments = parser.parse_args()
if arguments.year:
    print('----------Title---------------Year---\n')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + years[i] + '\n')
elif arguments.rate:
    print('----------Title---------------Rate----')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + ratings[i] + '\n')
elif arguments.all:
    print('----------Title---------------Rate--Year--')
    for i, value in enumerate(titles):
        print(str(i + 1) + '. ' + titles[i] + ' - ' + ratings[i] + 
              ' - ' + years[i] + '\n')
elif arguments.histogram == 'rating':
    print('Histogram for quantity of films for each rating')
    for key in sorted(rating_frequency):
        print(key + ': ' + '+' * rating_frequency[key] +
              ' ' + str(rating_frequency[key]) + '\n')
elif arguments.histogram == 'year':
    print('Histogram for quantity of films for each year')
    for key in sorted(year_frequency):
        print(key + ': ' + '+' * year_frequency[key] +
              ' ' + str(year_frequency[key]) + '\n')
else:
    with open(arguments.output + '.txt', 'w', encoding='UTF-8') as file:
        for i, value in enumerate(titles):
            file.write(str(i + 1) + '. ' + titles[i] + ' - ' + 
                       ratings[i] + ' - ' + years[i] + '\n')
    print('Data was successfully written to the file.')
