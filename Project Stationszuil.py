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


#Bericht infrastructuur

message = input('Voer hier uw bericht in: ')
blocked = False
if len(message) > 140:
    print('Uw bericht is te lang. Probeer het opnieuw.')
else:
    input = input('Voer uw naam in. Laat dit leeg, voor anoniem: ')
    if len(input) == 0:
        naam = 'anoniem'
    else:
        naam = input
    with open('blacklist', 'r') as file:
        for line in file:
            if line in message: #kijkt of er scheldwoorden in zitten
                blocked = True
            if line in naam:
                blocked = True
    if not blocked: #Zo niet, hoera!
        time = str(datetime.now())
        list = [naam, time, kiesStation(), message]
        invoer(list)
