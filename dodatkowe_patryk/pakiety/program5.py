def jakas_funkcja(x):
    # "import lokalny"
    from modul import pole_kwadratu
    print(pole_kwadratu(x))

# nie można skorzystać poza funkcją
# pole_kwadratu(8)

# nawet gdy funckje wywołuję wielokrotnie, albo wiele takich funkcji, to moduł importuje się raz

print('AAA')
jakas_funkcja(7)
print('BBB')
jakas_funkcja(6)
print('CCC')

