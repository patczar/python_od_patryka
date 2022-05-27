# Nieskończony generator liczb parzystych

def parzyste():
    liczba = 0
    while True:
        yield liczba
        liczba += 2


# Samo wywołanie nie wykonuje tej pętli. Tworzony jest generator.
g = parzyste()
print(g)

# Dopiero umieszczenie w pętli for, albo wielokrotne wywoływanie next, albo konwersja na listę / zbióre / itp.
# spowoduje wykonanie tej pętli i dostarczanie kolejnych wartości.
for x in parzyste():
    print(x)
