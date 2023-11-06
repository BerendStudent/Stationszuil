import csv
import os
import psycopg2

data = []
email = input('Voer uw email adres in: ')
naam = input('Voer uw naam in: ')
connection = psycopg2.connect(
    database="Project Stationszuil",
    user="Cursor",
    password="Password",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

with open('data.csv', 'r') as file:
    with open('reviews.csv', 'a') as newFile:
        reader = csv.reader(file)
        writer = csv.writer(newFile)
        for row in reader:
            print(str(row))
            goed = input('Goedgekeurd, Y/N: ')
            if goed == 'Y':
                row.append(naam)
                row.append(email)
                writer.writerow(row)
                print("Goedgekeurd.")
            elif goed == 'N':
                print("Afgekeurd.")
            else:
                print('Y of N')
        os.remove('data.csv')
        print('Alles is nagekeken.')
