# Na czy polega różnica między niemutowalnym str a mutowalną listą?
strA = 'Ala'
strB = strA

print('strA:', strA)
print('strB:', strB)

# strA[0] = 'O'
strA += ' ma kota'

print('strA:', strA)
print('strB:', strB)
print()

listA = ['Ala']
listB = listA

print('listA:', listA)
print('listB:', listB)

listA[0] = 'Ola'
listA += ['kot']
# to by dało inny efekt:
# listA = listA + ['kot']

print('listA:', listA)
print('listB:', listB)
