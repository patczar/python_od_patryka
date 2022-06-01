# W Pythonie można dopisywać else do pętli while i for

# Tak zapisany else wykona się jeden raz, gdy warunek niebędzie już prawdziwy.
# Może to być od razu, ale nawet gdy pętla while wykona się kilka razy (bo warunek był prawdziwy)
# i dopiero po kilku obrotach się zakończy, to else też się wykona.
x = 5
while x < 10:
    print(x, end=', ')
    x += 1
else:
    print('else', x)
print()

# Sens użycia else zobaczymy dopiero, gdy połączymy to z break.
# Gdy pętla kończy się normalnie → na końcu wykonuje się else
# Gdy pętla jest przerywania break → else się nie wykonuje
# Inaczej mówiąc break wychodzi poza całą pętlę, pomija również else.

x = 4
while x < 9: # zmień na 6
    print(x, end=', ')
    if x % 7 == 0:
        break
    x += 1
else:
    print('else', x)
print('za pętlą, x =', x)
