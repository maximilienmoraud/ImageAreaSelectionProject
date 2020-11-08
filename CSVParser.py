#import pandas as pd
import csv

def ReadCategorie():
    with open('categorie.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            return row

def WriteCategorie(list):
    with open('categorie.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(list)

def ImportForm():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=":")
        for row in csv_reader:
            return row

def ExportForm(list):
    with open('data.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=':', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(list)
