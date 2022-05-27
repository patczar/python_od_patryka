def bold(f):
    def wrapper(*args, **kwargs):
        napis = f(*args, **kwargs)
        return f'<b>{napis}</b>'
    return wrapper

# Zmodyfikowana wersja funkcji, którą zwraca dekorator, może być zdefiniowana
# nie tylko konstrukcją def
def italic(f):
    return lambda *args, **kwargs: f'<i>{f(*args, **kwargs)}</i>'

@bold
@italic
def foo(arg):
    return f'To jest {arg}'

foo('Ala')
print(foo('Ola'))

@italic
@bold
def zaproszenie(jezyk, miasto, czas):
    return f'Zapraszamy na kurs języka {jezyk}, który odbędzie się w {miasto} i będzie trwać {czas} dni.'

print(zaproszenie('Python', 'Warszawa', 20))
print(zaproszenie('SQL', 'Kraków', 8))


