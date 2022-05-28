from setuptools import setup, find_packages

setup(
    name='mathematica',
    version='1.0.0',
    description='Math utils.',
    packages=find_packages(exclude=['mathematica.tests']),
)


# Aby zbudować paczkę w formie zipa używamy:
# python setup.py sdist --format=zip
# - to daje wersję ze źródłami, którą łatwiej zainstalować

# lub ewentualnie
# python setup.py bdist
# - co daje wersję "binarną"/"skompilowaną", którą trudniej zainstalować - może być to nieprzenośne między systemami

# Po zbudowaniu paczki za pomocą sdist w docelowej lokalizacji można wykonać polecenie
# pip install mathematica-1.0.0.zip
# i pakiet oraz jego moduły staną się dostępne
