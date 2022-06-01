import subprocess

print('Początek Pythona')

#ERR subprocess.run('ls -l')

# OK
# Gdy uruchamiany program ma otrzymać parametry, to do run przekazujemy listę
# gdzie na początku jest samo polecenie, a potem jego argumenty.
subprocess.run(['ls', '-l'])
print('--------')

result = subprocess.run(['python', r'/home/patryk/PycharmProjects/pythonProject/p01_podstawy/hello.py'])

print('Proces zakończony:', result)
print('Kod zakończenia:', result.returncode)
