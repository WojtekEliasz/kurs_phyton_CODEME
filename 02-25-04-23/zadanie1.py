#1

liczba = float(input("podaj liczbę"))

if liczba % 3 == 0:

    print ("to jest liczba podzielna przez 3")
else:
    ("to nie jest liczba podzielna przez 6""")

#3
user1 = float(input("user1 podaj ocenę książki od 0 do 10: "))
user2 = float(input("user2 podaj ocenę książki od 0 do 10: "))
user3 = float(input("user3 podaj ocenę książki od 0 do 10: "))

ocena = ((user1+user2+user3)/3)
ocena = round(ocena,2)
print ("srenia ocena wynosi: ", ocena)


if ocena >= 7:
    print("bardzo dobrze")
if (ocena < 7) and (ocena > 5):
    print("przeciętnie")
else:
    print("nie warta uwagi")

#5

password = input("podaj hasło :")

if password.isupper() and password.islower() and password.isdigit() and len(password) >= 8:

    print("ok")

if len(password) < 8:
    print("za krotkie")
if password.isalnum() and password.isalpha():
    print("brakuje co najmniej jednej cyfry")
if password.isalnum() and password.isdigit():
    print("brakuje litery")
if password.lower():
    print("brakuje dużej litery")
if password.isupper():
    print("brakuje małej litery")

    print(f' [not] hasło to', password)



#FOR


my_list = ["ada", "ruby", "julia"]

for step in my_list:
    print("hello ", step)

"""
for step in range(1, 50, 2):
    print("krok: ", step)
"""
"""
pa = ""
magic = "hokuspokus"
from num in range(2, 10, 2):
    pa = pa +str(num) +magic[num]
print(pa)
"""

lista_rzeczy = ["tel", "cash", "ID", "keys", "map", "wath"]

for i in lista_rzeczy:
    print(i)

sum_num = 0

for sum in range(1, 11):
    sum_num += sum  #i=iplus
    print(sum_num)

tempf = 0
while tempf <= 200:
    print("temp w C =:", round(5/9 * (tempf - 32), 2))
    tempf += 20


lista_imion = print("podaj imiona oddzielone spacjami :")

tablica = lista_imion.replace(" ", ", ")

print(tablica)