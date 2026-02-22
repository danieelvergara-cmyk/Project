studenter = {
    'Anna': 85,
    'Bo': 92,
    'Celia': 78
}

for namn, betyg in studenter.items():
    print(f'{namn}: {betyg}')





import json
person = {
    'namn': 'Alice',
    'ålder': 30,
    'stad': 'Stockholm'
}

print(person['namn'])
print(person['ålder'])
print(person['stad'])

for nyckel, värde in person.items():
    print(f'{nyckel}: {värde}')


bil = {
    'märke': 'BMW',
    'år' : 1990,
    'mil' : 39
}
print(bil['märke'])
print(bil['år'])
print(bil['mil'])

for nyckel, värde in bil.items():
    print(f'{nyckel}: {värde}')



användare = [
        {'namn': 'eme', 'år': 17, 'roll': 'vd'},
        {'namn': 'dani', 'år': 24, 'roll': 'vd'},
        {'namn': 'angi', 'år': 20, 'roll': 'tränare'}
]
for vd in användare:
    if vd['roll'] == 'tränare':
        print(vd['namn'], 'är tränare')
    else:
        print(vd['namn'], 'är vanlig i hemmet')
for vd in användare:
    if vd['år'] >= 18:
        print(vd['namn'], 'är 18+ år')
    else:
        print(vd['namn'], 'under 18')



dannes_anställda = [
            {'namn': 'Camilo', 'år': 50},
            {'namn': 'Eme', 'år': 17.5}
]
for namn in dannes_anställda:
    if namn['namn'] == 'Camilo':
        print(namn['namn'], 'är biträdande')



























kunder = [
    {'namn': 'Angi', 'ålder': 20},
    {'namn': 'Dane', 'ålder': 24}
]
for namn in kunder:
    if kunder[namn] == 'Angi' 'Dane':
        print(f'{kunder[namn]}')




#min version ovan under rättad version 9 januari

        kunder = [
    {'namn': 'Angi', 'ålder': 20},
    {'namn': 'Dane', 'ålder': 24}
]

for kund in kunder:  # ← Ändrat från 'namn' till 'kund'
    if kund['namn'] == 'Angi' or kund['namn'] == 'Dane':  # ← Lagt till 'or'
        print(kund['namn'])  # ← Fixat print
kunder = [
    {'namn': 'Angi', 'ålder': 20},
    {'namn': 'Dane', 'ålder': 24}
]






bilar = [
    {'märke': 'porsche', 'model': 'a7'},
    {'märke': 'volvo', 'model': 'a5'}

]
for bil in bilar:
    if bil['märke'] == 'porsche':
        print(bil['märke'])