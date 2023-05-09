""" Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki,
które są na pozycjach parzystych. Wykonaj na dwa sposoby - za pomocą pętli oraz
przez sting slicing ( ‘abrakadabra’ -> ‘baaar’)."""

ciąg=input("podaj ciąg znaków :")

print("znaki na parzystych pozycjach to :", ciąg[1::2])



# lub
# pozycja = int(len(ciąg))
#
# for nr in range(1, pozycja+1, 2):
#
#
#     print("znaki na parzystych pozycjach to :", ciąg[nr:nr+1:])



        # Napisz grę - kamień (k) / papier (p) / nożyce (n).
        # Użytkownik podaje jedną z 3 figur.
        # Komputer losuje jedną z 3 figur.
        # Sprawdź kto wygrał tę rundę.
        # Zmień kod tak, by użytkownik mógł podac liczbę rund.
        # Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
        # Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’




# print('Gra papier kamień nożyce')
# import random
# liczba_rund = int(input("podaj liczbę rund :"))
# tablica = ['1 - papier', '2 - kamień', '3 - nożyce']
# print(tablica)
# licznik = 0
# scoregracz = 0
# scorepc = 0
# gracz = 4
#
# while licznik != liczba_rund and gracz != 0:
#     gracz = int(input('Wybierz jeden z elementów za pomoca cyfry, komputer już wylosował :'))
#     print('jeśli chcesz zakończyć wybierz "0" ')
#     pcet = (random.randint(1, 3))
#
#     print('twój wybór: ', gracz)
#     print('komputer :', pcet)
#
#     if gracz == pcet:
#         print("remis")
#     elif gracz == 1 and pcet == 2 or gracz == 2 and pcet == 3 or gracz == 3 and pcet == 1:
#         print("wygrałeś")
#         scoregracz = scoregracz + 1
#     elif gracz == 0:
#         print("koniec")
#     else:
#         print("przegrałeś")
#         scorepc = scorepc + 1
#
#
#
#     licznik = licznik + 1
#
# print("punktacja twoj vs pc:", scoregracz, 'do', scorepc)