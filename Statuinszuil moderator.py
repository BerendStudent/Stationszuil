import csv
import os
import psycopg2

stopped = False
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

def deleteLine(delete):
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        with open('temp.csv', 'w', newline='') as temp:
            writer = csv.writer(temp)
            for row in reader:
                writer.writerow(row)
    with open('data.csv', 'w') as file:
        writer = csv.writer(file)
        with open('temp.csv', 'r') as temp:
            reader = csv.reader(temp)
            for row in reader:
                if row != delete:
                    writer.writerow(row)
    os.remove('temp.csv')

def clearFile(file):
    with open(file, 'r+') as clearedFile:
        clearedFile.truncate(0)


with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    print('Voer STOP in om te stoppen.')
    for row in reader:
        if row == []:
            continue
        print(str(row))
        goed = input('Goedgekeurd, Y/N: ')
        if goed == 'Y':
            row.append(naam)
            row.append(email)
            query = """insert into Admins (Adminnaam, email) VALUES (%s, %s) ON CONFLICT DO NOTHING; 
            insert into berichten (naam, datum, stationsnaam, inhoud, Email) 
            VALUES (%s,%s,%s,%s,%s);"""
            invoer = (naam, email, row[0], row[1], row[2], row[3], email)
            cursor.execute(query, invoer)
            connection.commit()
            deleteLine(row)
            print("Goedgekeurd.")
        elif goed == 'N':
            deleteLine(row)
            print("Afgekeurd.")
        elif goed == 'STOP':
            stopped = True
            break
        else:
            print('Y of N')
    if not stopped:
        clearFile('data.csv')
    print('Alles is nagekeken.')
