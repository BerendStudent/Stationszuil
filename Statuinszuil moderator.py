import csv
import os
import psycopg2

data = []
email = input('Voer uw email adres in: ')
naam = input('Voer uw naam in: ')
connection = psycopg2.connect(
    database="Project Stationszuil",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()
while True:
    with open('data.csv', 'r') as file:
        with open('reviews.csv', 'a', newline='') as newFile:
            reader = csv.reader(file)
            writer = csv.writer(newFile)
            print('Voer STOP in om te stoppen.')
            for row in reader:
                print(str(row))
                goed = input('Goedgekeurd, Y/N: ')
                if goed == 'Y':
                    row.append(naam)
                    row.append(email)
                    writer.writerow(row)
                    query = """insert into Admins (Adminnaam, email) VALUES (%s, %s) ON CONFLICT DO NOTHING; 
                    insert into berichten (naam, datum, stationsnaam, inhoud, Email) 
                    VALUES (%s,%s,%s,%s,%s);"""
                    invoer = (naam, email, row[0], row[1], row[2], row[3], email)
                    cursor.execute(query, invoer)
                    connection.commit()
                    print("Goedgekeurd.")
                elif goed == 'N':
                    writer.writerow(row)
                    print("Afgekeurd.")
                elif goed == 'STOP':
                    break
                else:
                    print('Y of N')
            os.remove('data.csv')
            print('Alles is nagekeken.')
