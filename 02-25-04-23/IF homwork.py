
"""2 Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100,
wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”."""


num1 = input("podaj liczbę nr1 :")
num1 = float(num1.replace(",", "."))
num2 = input("podaj liczbę nr2 :")
num2 = float(num2.replace(",", "."))

sum = num1 + num2

if sum > 100:
    (print(sum))
else:
    print("koniec")

"""4 Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy 
niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis. """

text1 = input("podaj ciąg znaków : ")
l = len(text1)
n_of_a = text1.count('a')

if l>5 and n_of_a >0 :
    text2 = text1.replace('a', 'z')
    print(text2)
else :
        print("koniec.")

"""6 Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą
przez programistę wyświetl komunikat “gratulacje!”, w przeciwnym razie wyświetl “pudło!”."""


import random
quess = (random.randint(1,100))
#print(quess)
user = int(input("zgadnij liczbę ukrytą przez program od 1 do 100 :"))

if quess == user :
    print("brawo")
else :
    print("nie zgadłeś")


"""7 Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość."""

h = (input("podaj swoj wzrost w m ->"))
w = (input("podaj swoja wage w kg ->"))

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))

BMI = (w / h ** 2)

print("BMI wynosi", round(BMI, 2))

if BMI < 16 : print("wygłodzenie")
elif (BMI > 16 and BMI < 16.99): print("wychudzenie")
elif (BMI > 17 and BMI < 18.49): print("niedowaga")
elif (BMI > 18.50 and BMI < 24.99): print("waga prawidłowa")
elif (BMI > 25 and BMI < 29.99): print("nadwaga")
elif (BMI > 30 and BMI < 34.99): print("I stopień otyłości")
elif (BMI > 35 and BMI < 39.99): print("II stopień otyłości")
elif (BMI > 40 ): print("otyłość skrajna")

"""8 Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej."""

no1 = (input("podaj liczbę nr 1: "))
no2 = (input("podaj liczbę nr 2: "))
no3 = (input("podaj liczbę nr 3: "))

no1 = float(no1.replace(",", "."))
no2 = float(no2.replace(",", "."))
no3 = float(no3.replace(",", "."))

lista = [no1,no2,no3]

n = len(lista)

while n > 1:
    zamien = False
    for l in range(0, n - 1):
        if lista[l] > lista[l + 1]:
            lista[l], lista[l + 1] = lista[l + 1], lista[l]
            zamien = True
    n -= 1

    if zamien == False: break

print(lista)



