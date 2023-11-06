import csv
import os
import psycopg2


data = []
email = input('Voer uw email adres in: ')
naam = input('Voer uw naam in: ')


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
