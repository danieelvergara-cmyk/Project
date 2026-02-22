import json

# DEL 1: Spara dictionary (10 min)
print('--- DEL 1: Spara person till fil ---')

person = {
    'namn': 'Daniel',
    'ålder': 24,
    'stad': 'Stockholm'
}

# SPARA till fil
with open('person.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, indent=2, ensure_ascii=False)
print('✓ Sparat till person.json')
print('→ Kolla i mappen, du ser nu filen person.json!')

print('\n---\n')

# DEL 2: Läs från fil (10 min)
print('--- DEL 2: Läs från fil ---')

with open('person.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Läste från fil: {data}')
print(f"Namn: {data['namn']}")
print(f"Ålder: {data['ålder']}")
print(f"Stad: {data['stad']}")

print('\n---\n')

# DEL 3: Ändra och spara igen (10 min)
print('--- DEL 3: Ändra data ---')

# Ändra ålder
data['ålder'] = 25

# Lägg till ny nyckel
data['hobby'] = 'Programmering'

# Spara igen
with open('person.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print('✓ Ändrat och sparat!')
print(f'Ny data: {data}')

#under e uppgift 2:
# Efter DEL 3, lägg till:

print('\n---\n')
print('--- TESTA SJÄLV ---')

# Skapa din egen person
min_person = {
    'namn': input('Ditt namn: '),
    'ålder': int(input('Din ålder: ')),
    'stad': input('Din stad: ')
}

# Spara
with open('min_person.json', 'w', encoding='utf-8') as f:
    json.dump(min_person, f, indent=2, ensure_ascii=False)

print('✓ Din person sparad till min_person.json!')












print('\n---\n')
print('\n---\n')
# 1. Importera json
# 2. Skapa dictionary med namn och ålder
# 3. Spara till fil 'test.json'
# 4. Läs från filen
# 5. Skriv ut vad du läste





import json

# Skapa dictionary
person = {'namn': 'Daniel', 'ålder': 24}

# Spara
with open('test.json', 'w') as f:
    json.dump(person, f)

# Läs
with open('test.json', 'r') as f:
    data = json.load(f)

print(data)








import json

person = {'namn': 'Dani', 'ålder': 24}

with open('test.json', 'w') as f:
    data = json.dump(person, f)

with open('test.json', 'r') as f:
    data = json.load(f)

print(data)










import json

# Skapa kontakt
namn = input('Namn: ')
telefon = input('Telefon: ')
kontakt = {'namn': namn, 'telefon': telefon}

# Spara till fil
with open('min_kontakt.json', 'w', encoding='utf-8') as f:
    json.dump(kontakt, f, ensure_ascii=False, indent=4)

print('Kontakt sparad!')

# Ladda från fil
with open('min_kontakt.json', 'r', encoding='utf-8') as f:
    laddad_kontakt = json.load(f)

print(f"Laddad: {laddad_kontakt['namn']} - {laddad_kontakt['telefon']}")

