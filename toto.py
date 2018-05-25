import random

try:
    ileliczb = int(input("Ile losujemy?"))
    makslicza = int(input("Liczba max?"))
    if ileliczb > makslicza:
        print("Bledne dane")
        exit()
except ValueError:
    print("Bledne Dane")
    exit()
# lists

liczby = []
for i in range(ileliczb):
    liczba = random.randint(1, makslicza)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1
print("Wylosowane liczby: ", liczby)

#set
for i in range(3):
    print("Wytypuj %s z %s liczb: " %(ileliczb, makslicza))
    typy = set()
    i =0
    while i < ileliczb:
        try:
            typ = int(input("Podaj liczbe %s: " % (i +1)))
        except ValueError:
            print("Bledne dane")
            continue
        if typ not in typy:
            typy.add(typ)
            i = i + 1

    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x

print("Wylosowane liczby:", liczby)

