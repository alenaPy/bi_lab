"""Task2 working with argparser."""
import argparse

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

prsr = argparse.ArgumentParser()
prsr.add_argument("--year", help="Shows top 250 movies (title and year)",
                  default=False)
prsr.add_argument("--rate", help="Shows top 250 movies (title and rate)",
                  default=False)
prsr.add_argument("--all", help="Shows movie title, rate and year",
                  default=False)
prsr.add_argument("--histogram", help="Displays histogram for rating"
                                      " or for years (in text format)",
                  default=False)
prsr.add_argument("--output", help="Stores all data"
                                   " to specified filename file",
                  default=False)
args = prsr.parse_args()

for m in range(250):
    years.append(films[m][1])
dict_years = dict(sorted((i, years.count(i)) for i in years))
for m in range(250):
    film_rating.append(films[m][2])
dict_rate = dict(sorted((i, film_rating.count(i)) for i in film_rating))

if args.year:
    i = 0
    print("Top 250 movies (title and year)")
    for f in films:
        i += 1
        print("%d. %s YEAR: %s" % (i, f[0], f[1]))

if args.rate:
    i = 0
    print("Top 250 movies (title and rate)")
    for f in films:
        i += 1
        print("%d. %s RATE: %s" % (i, f[0], f[2]))

if args.histogram == "rate":
    print("Rate histogram: ")
    for f in dict_rate:
        print(str(f) + ": " + "|" * dict_rate[f] +
              " " + str(dict_rate[f]) + "\n")

elif args.histogram == "year":
    print("Year histogram: ")
    for f in dict_years:
        print(str(f) + ": " + "|" * dict_years[f] + " " +
              str(dict_years[f]) + "\n")

if args.all:
    i = 0
    print("Top 250 movies (title, rate, year)")
    for f in films:
        i += 1
        print("%d. %s , YEAR: %s, RATE: %s" %
              (i, f[0], f[1], f[2]))

if args.output:
    print("Write to " + args.output)
    output_file = open(args.output, "w")
    i = 0
    for f in films:
        i += 1
        output_file.write("%d. %s , YEAR: %s, RATE: %s \n" %
                          (i, f[0], f[1], f[2]))
    output_file.close()
