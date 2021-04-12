import sys

def kalkulator():
    rodzaj_działania = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: " ))
    skladnik_1 = int(input("podaj pierwszą liczbę "))
    skladnik_2 = int(input("Podaj druga liczbe "))
    if rodzaj_działania == 1:
        wynik = skladnik_2 + skladnik_1
        print("Dodaję %s i %s" % (skladnik_1, skladnik_2))
    elif rodzaj_działania == 2:
        wynik = skladnik_2 - skladnik_1
        print("Odejmuję %s i %s" % (skladnik_1, skladnik_2))
    elif rodzaj_działania == 3:
        wynik = skladnik_2 * skladnik_1
        print("Mnożę %s i %s" % (skladnik_1, skladnik_2))
    elif rodzaj_działania == 4:
        wynik = skladnik_2 / skladnik_1
        print("Dzielę %s i %s" % (skladnik_1, skladnik_2))
    else:
        exit(1)
    print("Oto wynik działania %s" % (wynik))
kalkulator()