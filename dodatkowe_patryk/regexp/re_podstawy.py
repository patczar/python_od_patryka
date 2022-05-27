import re

wzorzec1 = '[1-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]'
wzorzec2 = r'[1-2]\d{3}-((0[1-9])|(1[0-2]))-((0[1-9])|([1-2][0-9])|(3[0-1]))'

# w tej wersji w wyrażeniu zaznaczamy 3 "grupy"
# grupę oznacza się za pomocą nazwiasów okrągłych,
# ale żeby w innym miejscu nawiasy nie miały specjalnego znaczenia (nie tworzyły grupy),
# to dopisujemy na początku (?:  - wtedy to są "grupy anonimowe"
wzorzec3 = r'([1-2]\d{3})-((?:0[1-9])|(?:1[0-2]))-((?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))'

while True:
    tekst = input('Podaj tekst: ')
    if not tekst: break

    if re.match(wzorzec1, tekst):
        print('pasuje do wzorca1')
    else:
        print('nie pasuje do wzorca1')

    if re.match(wzorzec2, tekst):
        print('pasuje do wzorca2')
    else:
        print('nie pasuje do wzorca2')

    m = re.match(wzorzec3, tekst)
    if m:
        # dwa sposoby odczytania wartości grupy (czyli fragmentu, który pasował do (nazwiasów) we wzorcu:
        y = m.group(1)
        y = m[1]
        month = m[2]
        day = m[3]
        print(f'pasuje do wzorca3. y={y}, m={month}, d={day}')


