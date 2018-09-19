"""Task1 work with file IMDB rating."""

input_file = "ratings.list"
file_start = "New  Distribution  Votes  Rank  Title"
start = 0
top_films = 0
c = 0

films = []
years = []
film_rating = []

try:
    with open(input_file, "r") as film_file:
        for line in film_file:
            if file_start in line:
                start = 1
            elif start == 1 and (line.strip()) != 0:
                rate = line.strip().split("  ")[2]
                name_year = line.strip().split("  ")[3]
                f = name_year.split(" (")
                film_name = f[0]
                year = f[1][:4:]
                films.append([film_name, year, rate])
                c += 1
            if c == 250:
                break
except FileNotFoundError:
    print("The file wasn`t found!")
    exit()

films_250 = open("top250_movies.txt", "w")
for i in range(250):
    films_250.write("%d. %s \n" % (i + 1, films[i][0]))
films_250.close()

for i in range(250):
    years.append(films[i][1])

dict_years = dict(sorted((i, years.count(i)) for i in years))

years_file = open("years.txt", "w")
for i in dict_years:
    years_file.write((str(i) + ": " + "|" * dict_years[i] + " " +
                      str(dict_years[i]) + "\n"))
years_file.close()

film_rating = []
for i in range(250):
    film_rating.append(films[i][2])

dict_rate = dict(sorted((i, film_rating.count(i)) for i in film_rating))

rate_file = open("rating.txt", "w")
for i in dict_rate:
    rate_file.write(str(i) + ": " + "|" * dict_rate[i] +
                    " " + str(dict_rate[i]) + "\n")
