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

def ExportForm(list):
    with open('data.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=':', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(list)

def Existedeja(image, formnane):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=":")
        for row in csv_reader:
            if len(row)!=0:
                if (row[0]==image)&(row[2]==formnane):
                    return 1

def FiltreCategorie(image):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        list = []
        for row in csv_reader:
            if len(row) != 0:
                if row[0] == image:
                    if row[1] not in list:
                        list.append(row[1])
        return list

def FiltreName(image, categorie):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        list = []
        for row in csv_reader:
            if len(row) != 0:
                if (row[0] == image)&(row[1] == categorie):
                    list.append(row[2])
        return list

def SupprimeForm(image, categorie, name):
    lines = list()
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            if len(row) != 0:
                if (row[0] != image) & (row[1] != categorie) & (row[2] != name):
                    lines.append(row)
    with open('data.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(lines)