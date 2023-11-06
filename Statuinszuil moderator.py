import csv
import os
import psycopg2


data = []
email = input('Voer uw email adres in: ')
naam = input('Voer uw naam in: ')

def removeItem(num):
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        data.pop(num)
        for x in data:
            writer.writerow(x)

with open('data.csv', 'r') as file:
    with open('reviews.csv', 'a') as newFile:
        reader = csv.reader(file)
        writer = csv.writer(newFile)
        for row in reader:
            print(str(row))
            goed = input('Goedgekeurd, Y/N: ')
            if goed == 'Y':
                newFile.write(str(row))
                print("Goedgekeurd.")
            elif goed == 'N':
                print("Afgekeurd.")
            else:
                print('Y of N')
        os.remove('data.csv')
        print('Alles is nagekeken.')
