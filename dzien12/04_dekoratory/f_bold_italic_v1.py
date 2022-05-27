def bold(f):
    def wrapper(arg):
        napis = f(arg)
        return f'<b>{napis}</b>'
    return wrapper

# Zmodyfikowana wersja funkcji, którą zwraca dekorator, może być zdefiniowana
# nie tylko konstrukcją def
def italic(f):
    return lambda arg: f'<i>{f(arg)}</i>'

@bold
@italic
def foo(arg):
    return f'To jest {arg}'


foo('Ala')
print(foo('Ola'))
