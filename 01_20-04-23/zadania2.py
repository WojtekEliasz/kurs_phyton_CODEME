
#1 Czy 23 + 3 będzie się równać 15 + 12 ?

#2 Czy dzielenie 29 przez 7 bez reszty wynosi 5?

#3 Czy 27 podzielone przez 8 daje resztę 3?

#4 Wyświetl True, jeżeli liczba jest parzysta.

#5 Czy 43 - 13 będzie się równać 11 + 12 ?

#6 Czy dzielenie 129 przez 17 bez reszty wynosi 3?

#7 Czy 247 podzielone przez 5 daje resztę 2?


#1
print("#1")
a=23+3
b=15+12
print(bool(a == b))

#3
print("#3")
a=27
b=8
print(bool ((a%b) == 3))

#5
print("#5")
a=43-13
b=11+12
print(bool(a == b))


#7
a=247
b=5
print("#7")
print(bool ((a%b) == 2))

#dodatkowe
print("#dodatkowe")
a=17
print(bool((a % 2) == 0))