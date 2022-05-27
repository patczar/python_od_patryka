from subprocess import call

KATALOG_PROJEKTU = '/home/patryk/PycharmProjects/kpython-20201026/src/'

print('Zaraz zacznę')

call(['find', KATALOG_PROJEKTU, '-name', '*.py'])

print('Gotowe')
