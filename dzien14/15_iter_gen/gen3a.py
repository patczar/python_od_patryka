from typing import Generator


def parzyste(limit: int) -> Generator[int, None, None]:
    liczba = 0
    while liczba < limit:
        yield liczba
        liczba += 2


for x in parzyste(1000):
    print(x)
