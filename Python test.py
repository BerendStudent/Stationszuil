array = []

while True:
    invoer = input('Voer een getal in:')
    if invoer == 'stop':
        break
    else:
        getal = int(invoer)
        array.append(getal)
getal1 = 1
x = 0
for i in array:
    getal1 = getal1 * array[x]
    x = x + 1

print('Als je deze getallen vermenigvuldigd, is het resultaat: ', getal1)