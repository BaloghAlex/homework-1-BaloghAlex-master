import sys

from finance.model import Valuta, KriptoValuta


def main():
    if len(sys.argv) < 2:
        raise NameError("Kevés argumentum!")
    if sys.argv[1] < 1:
        raise NameError("Helytelen argumentum!")
    lista = []
    for i in range(sys.argv[1]):
        sor = input()
        sor = sor.strip().split(";")
        if len(sor)==3:
            valuta = Valuta(sor[0], sor[1], float(sor[2]))
            lista.append(valuta)
        if len(sor)==4:
            valuta = KriptoValuta(sor[0], sor[1], float(sor[2]), sor[3])
            lista.append(valuta)
    lista = sorted(lista, key=lambda x: (-x.arfolyam, x.nev, x.jeloles))
    for valuta in lista:
        print(valuta)


if __name__=="__main__":
    main()