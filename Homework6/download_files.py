"""Solution for Download and extract data."""
import argparse
import csv
import io
import json
import os
from PyPDF2 import PdfFileReader
import requests
import ssl
import tarfile
import urllib.request
import xml.etree.cElementTree as ET
import yaml
# This method invoked for resolving issues with requests lib certificates
ssl.enum_certificates('CA')


def pdf_download():
    """Download some pdf file."""
    file_path = 'D:\Artsiom_Barysionak\Python\Homework6\\file.pdf'
    urllib.request.\
        urlretrieve('http://pilomaterialy-timber.com/'
                    'wp-content/uploads/'
                    '2012/09/rake-reyki-sosna-brusok-'
                    'price-list-Sunrise-Ltd-Kiev.pdf',
                    file_path)
    print('PDF file has been successfully downloaded. Check it at ' +
          file_path)


def pdf_show():
    """Show content of some pdf file."""
    url = 'http://pilomaterialy-timber.com/wp-content/uploads' \
          '/2012/09/rake-reyki-sosna-brusok-price-list-Sunrise-Ltd-Kiev.pdf'
    data = requests.get(url).content
    reader = PdfFileReader(io.BytesIO(data))
    contents = reader.getPage(0).extractText()
    return contents


def gz_extract():
    """Extract .gz file."""
    file_path = 'D:\Artsiom_Barysionak\Python\Homework6\\file.tar.gz'
    urllib.request.\
        urlretrieve('https://osdn.net/frs/g_redir.php?m=kent'
                    '&f=od1n%2Fsamples.tar.gz',
                    file_path)
    sample = tarfile.open('file.tar.gz', "r:gz")
    sample.extractall()
    print('gz archive has been successfully extracted. Check it at ' + 
          file_path)


def gz_show():
    """Show content of .gz file."""
    url = 'https://osdn.net/frs/g_redir.php?m=kent&f=od1n%2Fsamples.tar.gz'
    data = requests.get(url).content
    with tarfile.open(data, "r:gz") as sample:
        print(sample.list())


parser = argparse.\
    ArgumentParser(description='Download some file. File type can be'
                               ' specified (pdf or tar.gz),'
                               'otherwise all these files will be downloaded.',
                   add_help=True)
parser.\
    add_argument('--download', type=str, const='all', nargs='?',
                 help='specify pdf, tar.gz or nothing to download both files')
parser.add_argument('--show', type=str,
                    help='show file content (pdf or tar.gz).')
parser.add_argument('--format', type=str,
                    help='specify what format convert data to')
arguments = parser.parse_args()
pdf_exists = \
    os.path.isfile('D:\Artsiom_Barysionak\Python\Homework6\\file.pdf')
gz_exists = \
    os.path.isfile('D:\Artsiom_Barysionak\Python\Homework6\\file.tar.gz')

# Configure actions for downloading files.
if arguments.download == 'pdf':
    if pdf_exists:
        print('PDF file already exists.')
    else:
        pdf_download()
elif arguments.download == 'tar.gz':
    if gz_exists:
        print('tar.gz file already exists.')
    else:
        gz_extract()
elif arguments.download == 'all':
    if pdf_exists and not gz_exists:
        gz_extract()
        print('PDF file already exists.')
    elif not pdf_exists and gz_exists:
        pdf_download()
        print('tar.gz file already exists.')
    elif not pdf_exists and not gz_exists:
        gz_extract()
        pdf_download()
    else:
        print('Files already exist.')

# Show file content.
elif arguments.show == 'pdf':
    print(pdf_show())
elif arguments.show == 'tar.gz':
    gz_show()

# Convert data to chosen format and write it into the file.
elif arguments.format == 'json':
    with open('data.json', 'w') as json_output:
        json.dump(pdf_show(), json_output)
    print('Data has been successfully loaded into json file.')
elif arguments.format == 'xml':
    root = ET.Element('data')
    items = ET.SubElement(root, 'items')
    items.text = pdf_show()
    tree = ET.ElementTree(root)
    tree.write('data.xml')
    print('Data has been successfully loaded into xml file.')
elif arguments.format == 'csv':
    with open('data.csv', 'w') as csv_output:
        csv_writer = csv.writer(csv_output)
        csv_writer.writerow(pdf_show())
    print('Data has been successfully loaded into csv file.')
elif arguments.format == 'yaml':
    with open('data.yaml', 'w') as yaml_output:
        yaml.dump(pdf_show(), yaml_output, default_flow_style=False)
    print('Data has been successfully loaded into yaml file.')
else:
    print('Invalid choice.')
