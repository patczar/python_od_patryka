import subprocess

KATALOG_PROJEKTU = '/home/patryk/PycharmProjects/kpython-20201026/src/'

print('Zaraz zacznę')

result = subprocess.run(['find', KATALOG_PROJEKTU, '-name', '*.py'],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = result.stdout
tekst = output.decode()
linie = tekst.splitlines(keepends=False)

for linia in linie:
    print('*', linia)

print('Gotowe')
