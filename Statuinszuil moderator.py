import csv


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

def moderate(item):
    print(str(item))
    goed = input('Goedgekeurd, Y/N: ')
    if goed == 'Y':
        return True
    elif goed == 'N':
        return False
    else:
        print('Y of N')

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    writer = csv.writer(file)
    for row in reader:
        x = moderate(row)
        if x:
            print('YES!')
        elif not x:
            print('NO!')
            #removeItem(row)


