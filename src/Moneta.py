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
