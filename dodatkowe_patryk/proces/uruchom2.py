from subprocess import call

KATALOG_PROJEKTU = '/home/patryk/PycharmProjects/kpython-20201026/src/'

print('Zaraz zacznę')

with open('stdout.txt', mode='wb') as wyjscie, open('stderr.txt', mode='wb') as bledy:
    result = call(['find', KATALOG_PROJEKTU, '-name', '*.py'], stdout=wyjscie, stderr=bledy)
    print('result:', result)

print('Gotowe')
