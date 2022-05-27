def powitaj():
    print('Witamy serdecznie')

def pozegnaj():
    print('Do zobaczenia!')


# Funkcję mogę nie tylko wywołać (dopisując nawiasy () )
powitaj()

# Mogę zapisać ją do zmiennej
jakas_funkcja = powitaj
# Teraz w zmiennej jest funkcja (niektórzy powiedzą "wskaźnik do funkcji")
print(jakas_funkcja)
# zresztą to samo widać gdy
print(powitaj)

# Ale przede wszystkim mogę funkcję uruchomić poprzez tę zmienną
jakas_funkcja()

jakas_funkcja = pozegnaj
jakas_funkcja()

# Podmienić można też funkcję kryjącą się pod nazwami użytymi w def
pozegnaj = powitaj
pozegnaj()

jakas_funkcja() # tu jest jeszcze stare pożegnaj
print()

# Łatwo przez pomyłkę podmienić jedną z globalnych funkcji Pythona

x = 150
y = 190

print(min(x,y))

min = x if x < y else y
print(min)

# To spowodowało, że teraz nie mogę użyć funkcji globalnej min
#ERR print(min(x,y))

# Dlatego lepiej byłoby użyć nazwy niekolidującej z niczym innym
minimum = x if x < y else y
print(minimum)
