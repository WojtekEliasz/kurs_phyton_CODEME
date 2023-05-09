"""Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty
co należy pokolei dodać. Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”."""

lista_skladnikow = ['1 jajko', 'cebula', 'sol', 'pieprz', 'lyzka oliwy', 'użyj formy']

print(lista_skladnikow)
print("polacz składniki:", "\n")


for _n, ls in enumerate(lista_skladnikow):
    print(ls)
    if _n <= 4:
        print("potem ")
    if _n == 5:
        print("użyj piekarnika")

"""Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8)."""

ilosc_silnia=input("podaj liczbę od 0 do 8 a policze silnię: ")

print(ilosc_silnia)
ilosc_silnia = int(ilosc_silnia)
if ilosc_silnia <= 8 and ilosc_silnia > 0:
    print(ilosc_silnia,"! wynosi:")
    wynik = 1
    for krok in range(ilosc_silnia):
        wynik = (wynik) * (krok +1)
        print(krok + 1, "*", end=" ")
    print("wynik wynosi :", wynik)

else:
    print("liczba z poza zakresu")