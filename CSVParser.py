#import pandas as pd
import csv
import GraphicalInterface

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

def ExisteDeja(image, formnane):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=":")
        for row in csv_reader:
            if len(row)!=0:
                if (row[0]==image)&(row[2]==formnane):
                    return True
    return False

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

def SupprimeForm(test, image, categorie, name):
    print(GraphicalInterface.tempcategorie)
    print(GraphicalInterface.tempname)
    print(image)
    print(categorie)
    print(name)
    with open('temp.csv', mode='a') as csv_temp:
        csv_writer = csv.writer(csv_temp, delimiter=':', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        with open('data.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=':')
            for row in csv_reader:
                if len(row) != 0:
                    if (row[0] == image)&(row[1] == categorie)&(row[2] == name):
                        print('supprime')
                    else:
                        csv_writer.writerow(row)

    with open('data.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=':', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow('')

    with open('data.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=':', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        with open('temp.csv', mode='r') as csv_temp:
            csv_reader = csv.reader(csv_temp, delimiter=':')
            for row in csv_reader:
                if len(row) != 0:
                    csv_writer.writerow(row)

    with open('temp.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=':', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow('')

def RecupCoord(image_name, category, form_name):
    form_type = None
    scale = None
    coords = []

    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

        for line in csv_reader:
            if line: # On verifie que la liste ne soit pas vide
                if line[:3] == [image_name, category, form_name]:
                    form_type = line[3]
                    scale = float(line[5])
                    for points in line[4][2:-2].split('), ('):
                        x, y = point.split(', ')
                        coords.append((int(x), int(y)))
                    break

    return form_type, coords, scale
