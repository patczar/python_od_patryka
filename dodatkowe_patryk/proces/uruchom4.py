import subprocess

print('Zaraz zacznę')

# Tutaj efekt, który daje capture_output=True, uzyskujemy wpisując specjalną wartość PIPE
# do parametrów stdout i stderr
result = subprocess.run(['find', '..', '-name', '*.py'],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output = result.stdout
tekst = output.decode()
linie = tekst.splitlines(keepends=False)

for linia in linie:
    print('*', linia)

print('Gotowe')
