"""Labwork6."""

import argparse
from collections import OrderedDict
import csv
import io
import json
import os
import requests
import yaml
import zipfile

prsr = argparse.ArgumentParser()
prsr.add_argument("--format", help="Shows data in input format",
                  default=False)
args = prsr.parse_args()
csv_file = "restaurant-and-market-health-inspections.csv"

exs_file = os.path.isfile(csv_file)

if not exs_file:
    file_url = "https://www.kaggle.com/cityofLA/" \
               "la-restaurant-market-health-data/downloads/" \
               "la-restaurant-market-health-data.zip/22"
    file_get = requests.get(file_url)
    data = zipfile.ZipFile(io.BytesIO(file_get.content))
    data.extractall()
    data.close()
    print("Archive was extracted successfully")
else:
    print("File %s exists" % csv_file)

if args.format == "csv":
    with open(csv_file) as i_file:
        csv_rd = csv.reader(i_file)
        with open("output_file.csv", "w", newline="") as write_file:
            writer = csv.writer(write_file)
            for row in csv_rd:
                writer.writerow(row)
                print(", ".join(row))

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
    with open("json_in_file.json", "w") as json_file:
        json.dump(output, json_file)
        json_file.write("\n")

if args.format == "xml":
    csv_in_file = csv.reader(open(csv_file))
    xml_in_file = open("xml_in_file.xml", "w")
    xml_in_file.write('<?xml version="1.0"?>' + "\n")
    xml_in_file.write("<csv_data>" + "\n")
    rNum = 0
    for r in csv_in_file:
        if rNum == 0:
            tags = r
        else:
            xml_in_file.write("<r>" + "\n")
            for i in range(len(tags)):
                xml_in_file.write("    " + "<" + tags[i] + ">" +
                                  r[i] + "</" + tags[i] + ">" + "\n")
                xml_in_file.write("</r>" + "\n")
            rNum += 1
        xml_in_file.write("</csv_data>" + "/n")
        xml_in_file.close()

if args.format == "yaml":
    in_file = open(csv_file, "r")
    out_file = open("yaml_in_file.yaml", "w")
    items = []

    def convert_to_yaml(str):
        """Covert input string to yaml."""
        item = {
            "serial_number": str[0],
            "activity_date": str[1],
            "facility_name": str[2],
            "score": str[3],
            "grade": str[4],
            "service_code": str[5],
            "service_description": str[6],
            "employee_id": str[7],
            "facility_address": str[8],
            "facility_city": str[9],
            "facility_id": str[10],
            "facility_state": str[11],
            "facility_zip": str[12],
            "owner_id": str[13],
            "owner_name": str[14],
            "pe_description": str[15],
            "program_element_pe": str[16],
            "program_name": str[17],
            "program_status": str[18],
            "record_id": str[19]
        }
        items.append(item)
    try:
        reader = csv.reader(open(csv_file, "r"))
        next(reader)
        for i, line in enumerate(reader):
            convert_to_yaml(line)
        out_file.write(yaml.dump(items, default_flow_style=False))
    finally:
        in_file.close()
    out_file.close()
