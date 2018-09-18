"""Parse file with IMDB ratings and put result in separate .txt files."""

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
