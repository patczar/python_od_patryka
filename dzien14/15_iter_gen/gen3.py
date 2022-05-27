def parzyste(limit):
    liczba = 0
    while liczba <= limit:
        yield liczba
        liczba += 2


for x in parzyste(1000):
    print(x)
