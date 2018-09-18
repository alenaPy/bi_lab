"""Labwork4 Natallia Haisionak."""

s = 'New  Distribution  Votes  Rank  Title'
dataStart = 0
counter = 0
f = 'ratings.list'
movies = []
try:
    with open(f, 'r') as fp:
        for line in fp:
            if s in line:
                dataStart = 1
            elif dataStart == 1 and len((line.strip())) != 0:
                rate = line.strip().split('  ')[2]
                b = line.strip().split('  ')[3]
                c = b.split(' (')
                name = c[0]
                year = c[1][0:4:1]
                movies.append([name, year, rate])
                counter += 1
            if counter == 250:
                break
except FileNotFoundError:
    print('File not found')

movies_names = open("top250_movies.txt", "w")
for i in range(250):
    movies_names.write(movies[i][0] + '\n')
movies_names.close()

# List of years.

years = []
for i in range(250):
    years.append(movies[i][1])

d_years = dict((i, years.count(i)) for i in years)

years_list = open("years.txt", "w")
for i in d_years:
    years_list.write(str(i) + ' ' + str(d_years[i]) + '\n')
years_list.close()

# List of ratings.

r = []
for i in range(250):
    r.append(movies[i][2])

d_rate = dict((i, r.count(i)) for i in r)

rate_list = open("rating.txt", "w")
for i in d_rate:
    rate_list.write(str(i) + ' ' + str(d_rate[i]) + '\n')
rate_list.close()
