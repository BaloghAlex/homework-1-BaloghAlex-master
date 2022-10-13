from functools import total_ordering


@total_ordering
class Valuta:
    nev: str
    jeloles: str
    __arfolyam: float

    def __init__(self, nev, jeloles, arfolyam):
        self.nev = nev
        self.jeloles = jeloles
        self.__arfolyam = arfolyam

    @property
    def arfolyam(self):
        return self.__arfolyam

    @arfolyam.setter
    def arfolyam(self,value):
        self.__arfolyam=value

    def __repr__(self):
        return self.nev + ", " + self.jeloles + ", " + str(self.arfolyam)

    def __str__(self):
        return self.jeloles + "(" + self.nev + "): $" + str(self.arfolyam)

    def __eq__(self, other):
        return isinstance(other, Valuta) and self.nev==other.nev and self.jeloles==other.jeloles and self.arfolyam==other.arfolyam

    @staticmethod
    def erosebbek(lista, arfolyam):
        eros = []
        for elem in lista:
            if elem.arfolyam>arfolyam:
                eros.append(elem.jeloles)
        return eros

    def __lt__(self, other):
        if self.arfolyam < other.arfolyam:
            return True
        else:
            if self.nev >= other.nev:
                return False
            else:
                if self.jeloles >= other.jeloles:
                    return False
                else:
                    return True


class KriptoValuta(Valuta):
    __tervezo: str

    def __init__(self,nev,jeloles,arfolyam,tervezo):
        super().__init__(nev,jeloles,arfolyam)
        self.__tervezo = tervezo

    @property
    def tervezo(self):
        return self.__tervezo

    @tervezo.setter
    def tervezo(self,value):
        self.__tervezo=value

    def __repr__(self):
        return super().__repr__() + ", " + self.tervezo

    def __str__(self):
        return super().__str__() + ", @" + self.tervezo


