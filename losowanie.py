import random
licznik = 1
liczba = random.randint(1, 12)
print("Wylosowana liczba: ", liczba)
while liczba != 7:
    liczba = random.randint(1, 12)
    print("Wylosowana liczba: ", liczba)
    licznik += 1
print("Ilosc losowan: ", licznik)

