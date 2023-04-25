
# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.
print(" 1 Stwórz zmienną przechowującą wyraz....")
txt_string = input('podaj zmienny tekst o dł nieparzystej >7: ')
nieparzysty = (len(txt_string)) % 2
print(bool(nieparzysty))

if nieparzysty == True and len(txt_string) > 7:
    mid_txt = (len(txt_string)//2)
    mid_chars = txt_string[mid_txt - 1 : mid_txt + 2]

    print("trzy środkowe litery to", mid_chars)
else:
    print("podana ilość znaków jest parzysta lub mniejsza niż 7")


#Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
print(" \n 2 Stwórz dwie zmienne s1 i s2...")

S1 = input("podaj dowolny tekst nr 1:")
S2 = input("podaj dowolny tekst nr 2:")

midS1 = (len(S1)//2)
print(S1[:midS1], S2, S1[midS1:])


""" 
    Do zmiennej quote przypisz zdanie:

    „Honesty is the first chapter in the book of wisdom.”, a następnie:

    Policz wszystkie znaki w napisie

    Nie modyfikując zmiennej wyświetl słowo wisdom

    Wyświetl tylko pierwszą połowę tekstu

    Wyświetl tylko kropkę

    Wyświetl od połowy tylko co trzecią literę cytatu

    Wyświetl ‘Hnsyi h is hpe ntebo fwso.’

    Wyświetl cały cytat odwrotnie

    Zamień wisdom na słowo friendship
"""
print("\n 3 Do zmiennej quote przypisz zdanie...")
quote =('Honesty is the first chapter in the book of wisdom.')
ilosc_znakow = (len(quote))

print("\n",quote[(ilosc_znakow)-8:-1])  #tylko wisdom
print("\n",quote[:(ilosc_znakow//2)])  #od początku do połowy
print("\n",quote[ilosc_znakow-1:])   #tylko ostatnia kropka
print("\n",quote[ilosc_znakow//2::3])   #od połowy co trzecia litera
print("\n",quote[::2])                   #Wyświetl ‘Hnsyi h is hpe ntebo fwso.
print("\n",quote[::-1])                  #odwrotnie
print("\n", quote.replace('wisdom', 'friendship'))    #zamiana słowa
