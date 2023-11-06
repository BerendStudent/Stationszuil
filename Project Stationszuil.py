from datetime import datetime
import csv
import random


def kiesStation():
    with open('stations.txt') as f:
        stations = f.readlines()
        x = random.choice(stations)
        reply = x.strip('\n')
        return reply

def invoer(y):
    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(y)
        file.close()



message = input('Voer hier uw bericht in: ')
if len(message) > 140:
    print('Uw bericht is te lang. Probeer het opnieuw.')
else:
    input = input('Voer uw naam in. Laat dit leeg, voor anoniem: ')
    if len(input) == 0:
        naam = 'anoniem'
    else:
        naam = input
    time = str(datetime.now())
    list = [naam, time, kiesStation(), message]
    invoer(list)
    print(list[0])
