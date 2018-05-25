import random

def ustawienai():
    while True:
        try:
            ile = int(input("Podaj Ilosc typowanych liczb: "))
            maks = int(input("Podaj maksymalna losowana liczbe: "))
            if ile > maks:
                print("Bledne Dane")
                continue
            ilelos = int(input("Ile losowan: "))
            return (ile, maks, ilelos)
        except ValueError:
            print("Bledne dane")
            continue


def losujLiczby(ile, maks):
    liczby = []
    i = 0
    while i < ile:
        liczba = random.randint(1,maks)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            i = i + 1
    return liczby

def pobierztypu(ile, maks):
    print("Wytypuj %s z %s liczb: " %(ile, maks))
    typy = set()
    i = 0
    while i < ile:
        try:
            typ = int(input("Podaj liczbe %s: ") % (i + 1))
        except ValueError:
            print("Bledbe dane")
            continue

        if typ not in typy:
            typy.add(typ)
            i = i + 1
    return typy


def main(args):
    ileliczb, makslicza, ilerazy = ustawienai()

    liczby = losujLiczby(ileliczb, makslicza)

    for i in range(ilerazy):
        typy = pobierztypu(ileliczb, makslicza)
        trafione = set(liczby) & typy
        if trafione:
            print("\nIlość trafień: %s" % len(trafione))
            print("Trafione liczby: %s" % trafione)
        else:
            print("Brak trafień. Spróbuj jeszcze raz!")

        print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x

        print("Wylosowane liczby:", liczby)
        return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


