def fib(n):
    a, b = 0, 1
    for _ in range(n+1):
        yield a
        a, b = a+b, a


def main():
    n = int(input('Podaj liczbę liczb Fibonacciego: '))
    for i, f in enumerate(fib(n)):
        print(f'F({i}) = {f}')


if __name__ == '__main__':
    main()
