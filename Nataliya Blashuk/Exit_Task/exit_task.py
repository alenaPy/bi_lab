"""Exit task: Task1."""
import argparse
from collections import OrderedDict
import csv
import io
import json
import os
import requests
import zipfile

input_file = "ratings.list"
file_start = "New  Distribution  Votes  Rank  Title"
start = 0
top_films = 0
c = 0

films = []
years = []
film_rating = []

prsr = argparse.ArgumentParser()
prsr.add_argument("--year", help="Shows top 250 movies (title and year)",
                  action="store_true")
prsr.add_argument("--rate", help="Shows top 250 movies (title and rate)",
                  action="store_true")
prsr.add_argument("--all", help="Shows movie title, rate and year",
                  action="store_true")
prsr.add_argument("--histogram", help="Displays histogram for rating "
                                      "or year(in text format)",
                  default=False)
prsr.add_argument("--output", help="Stores all data"
                                   " to specified filename file",
                  default=False)
prsr.add_argument("--format", help="Shows data in input format",
                  default=False)
args = prsr.parse_args()

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
                if args.year is False and args.rate is False\
                        and args.histogram is False \
                        and args.all is False\
                        and args.output is False:
                    print("%d. %s " % (c, film_name))
            if c == 250:
                break

except FileNotFoundError:
    print("The file wasn`t found!")
    exit()

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

if args.histogram == "rating":
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

exs_file = os.path.isfile("restaurant-and-market-health-inspections.csv")

if not exs_file:
    try:
        file_url = "https://www.kaggle.com/cityofLA/" \
                   "la-restaurant-market-health-data/downloads/" \
                   "la-restaurant-market-health-data.zip/22"
        file_get = requests.get(file_url)
        data = zipfile.ZipFile(io.BytesIO(file_get.content))
        data.extractall()
        data.close()
    except zipfile.BadZipFile:
        print("The file is not zip file")

if args.format == "csv":
    with open(exs_file) as file:
        csv_rd = csv.reader(file)
        with open("outfile_csv.csv", "w", newline=" ") as write_file:
            writer = csv.writer(write_file)
            for row in csv_rd:
                writer.writerow(row)

if args.format == "json":
    f_names = ("serial_number", "activity_date", "facility_name",
               "score", "grade", "service_code", "service_description",
               "employee_id", "facility_address", "facility_city",
               "facility_id", "facility_state", "facility_zip",
               "owner_id", "owner_name", "pe_description",
               "program_element_pe", "program_name",
               "program_status", "record_id"
               )
    rst = []
    with open(exs_file, "r") as csv_file:
        reader = csv.DictReader(csv_file, f_names)
        for row in reader:
            entry = OrderedDict()
            for field in f_names:
                entry[field] = row[field]
            rst.append(entry)
    output = {"Restaurant": rst}
    with open("file.json", "w") as json_file:
        json.dump(output, json_file)
        json_file.write("\n")
