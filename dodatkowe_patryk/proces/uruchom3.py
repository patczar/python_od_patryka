import subprocess

# W tej wersji włączymy opcję zbierania outputu - to pozwala odczytać output po zakończeniu procesu.

# Wyjście programu jest zapamiętywane w RAM, a potem można to odczytać.

result = subprocess.run(['find', '..', '-name', '*.py'], capture_output=True)

print('Proces zakończony kodem', result.returncode)
print('Output:')
print(result.stdout)
# decode ?
