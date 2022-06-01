from subprocess import call

# W starszych wersjach Pythona zamiast run używało się call

print('Zaraz zacznę')

with open('stdout7.txt', mode='wb') as wyjscie, open('stderr7.txt', mode='wb') as bledy:
    result = call(['find', '..', '-name', '*.py'], stdout=wyjscie, stderr=bledy)
    print('result:', result)

print('Gotowe')
