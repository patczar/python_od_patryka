import json

with open('pracownicy.json', encoding='utf-8') as f:
    pracownicy = json.load(f)
# tutaj plik zostanie już zamknięty

print(pracownicy)

while True:
    cmd = input('Co chcesz zrobić? [d - dodaj, w - wypisz, q - koniec] ')
    if cmd == 'q':
        break
    elif cmd == 'd':
        nowy = {}
        nowy["imie"] = input('Podaj imię: ')
        nowy["nazwisko"] = input('Podaj nazwisko: ')
        nowy["rok_urodzenia"] = int(input('Podaj rok urodzenia: '))
        nowy["pensja"] = float(input('Podaj pensję: '))
        # print("nowy:", nowy)
        pracownicy.append(nowy)
        # dodajemy do listy w pamięci, a do pliku zostanie to zapisane po wciśnięciu q
    elif cmd == 'w':
        for p in pracownicy:
            #print(p)
            print(f'{p["imie"]} {p["nazwisko"]} ur.{p["rok_urodzenia"]} zarabia {p["pensja"]}')

with open('nowy.json', mode='w', encoding='utf-8') as f:
    json.dump(pracownicy, f)
