import random
hemligttal = random.randint(1, 20)
while True:
    gissning = int(input('tal?'))
    hemligttal != gissning
    if gissning == hemligttal:
        print(f'rätt gisning{gissning}')
        break
    if gissning > hemligttal:
        print('för högt')
    if gissning < hemligttal:
        print('för lågt')






import random
hemligttal = random.randint(1, 20)
gissning = 0
while gissning != hemligttal:
    gissning = int(input('skriv tal'))
    if gissning == hemligttal:
        print('rätt')
    if gissning < hemligttal:
        print('lågt')
    if gissning > hemligttal:
        print('högt')





def addera(a, b):
        return a + b
def multi(a, b):
    return a * b 
while True:
    tal1 = float(input('talq'))
    tal2 = float(input('taal'))
    operation = input('ange tecken ')
    if operation == '+':
        print(f'{addera(tal1, tal2)}')
    if operation == '*':
        print(f'{multi(tal1, tal2)}')
    elif operation == 'a':
        print('avslut')
        break






tasks = []
while True:
    val = input('välj')
    if val == '1':
        task = input('skriv uppgift')
        tasks.append(task)
        print('uppgift tillagd')
    elif val == '2':
        print(tasks)
    elif val == '3':
        print('avsluta')
        break



























import random
gissning = int(input('skriv tal'))
hemligttal = random.randint(1, 20)
while True:
    if gissning == hemligttal:
        print('rätt')
        break
    if gissning > hemligttal:
        print('för högt')
    if gissning < hemligttal:
        print('lågt')





import math
r = int(input('radien?')) 
def beräkna(r):
    area = 3.14 * r
    omkrets = r * 2
    return omkrets, area
omkrets = beräkna(r)
area = beräkna(r)
print(f'{omkrets}, {area}')