# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from decimal import *

class Moneta:
    lib = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]

    def __init__(self, waluta, wartosc):
        self.__waluta = waluta
        if wartosc in Moneta.lib:
            self.__wartosc = Decimal(wartosc)
        else:
            self.__wartosc = Decimal(0)

    def wartosc(self):
        return self.__wartosc
dolar = Moneta("USD",5)
euro = Moneta("EUR",1)
print(dolar.wartosc())
print(euro.wartosc())

# Seprint(euro.wartosc())e PyCharm help at https://www.jetbrains.com/help/pycharm/
