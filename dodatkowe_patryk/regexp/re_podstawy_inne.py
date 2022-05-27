import re

# Gdy mamy jakieś napisy
txt1 = 'ala.kowalska@gmail.com'
txt2 = 'toniejestemail#costam.net'

# i chcemy sprawdzić czy napis "pasuje do wzorca"
# najlepiej użyć wyrażeń regularnych (regular expression / regexp / regex / re)

wzorzec = '[a-z.]+@[a-z.]+[a-z]+'

if re.match(wzorzec, txt1):
    print('txt1 pasuje')
else:
    print('txt1 nie pasuje')

if re.match(wzorzec, txt2):
    print('txt2 pasuje')
else:
    print('txt2 nie pasuje')
