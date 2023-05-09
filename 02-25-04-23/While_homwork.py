
"""2) Napisz prostą grę, w której użytkownik musi zgadnąć liczbę
od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie."""



import random
numberB = (random.randint(0, 1))
numberA = input("Spróbuj zgadnąć liczbę ktorą mam w pamięci od 0 do 20: ")

while numberB != numberA:

    print("mój numer był to:", numberB)
    numberB = (random.randint(0, 1))
    numberA = input("nie udało się, jeszcze raz :")

  #  if numberA == numberB:
    #     break


print(" brawo udało się mój numer był to:", numberB)


"""1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. 
Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

    C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

Napisz rozwiązanie zarówno z użyciem pętli while jak i for."""

iteracja = 0

while iteracja != 200:
    temperatura = 5 / 9 * (iteracja - 32)

    iteracja = iteracja + 1

    print(round(temperatura))

