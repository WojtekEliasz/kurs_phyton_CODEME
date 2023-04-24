

# tupe zwraca jakie typu jest dana zmienna

wynik = 2+2*2.1
wynik = float(wynik)
print(wynik)
print(type(wynik))

# liczby zespolone
c=4+4j
d=1+2j

print (c*d)

#operatory porównania
# == równa się
# != nie równa się
# >
# <
# >=
# <=

print (1==1)

zmienna_eq = 1==5
print(type(zmienna_eq))

# True, False piszemy dużą literą
b = True
print(True)


#teksty

text1 = "ala"
text2 = "ala"
print(text1 != text2)

#logika

a=6
b=5

eq = a == b and 4 == 4 or a != b and not (4 == 5)


#zamiana zmiennych

a = int("4")
print(a)

b = bool(1)
print(b)
#boll zwraca wartość logiczną, można go użyć  czy teks jest pusty ("")

# operacje na tekstach

s = "2" + "2"
print(s)

x= """
komentarz
wielo
liniowy, który można wyrzucić na ekran
"""
#lub łamanie lini
y= "komentarz \n wielo \n liniowy"
print(x)
print(y)

#wyświetlanie litery pod indeksem (zaczyna od 0)
s = "hello"
print(s[2])

# długość tekstu
l= len(s)
print(l)
#wyciąganie ostatniej litery
print(s[l-1])
#lub to samo '-1' to ostatnia litera i lecimy w dół do '-5'
print(s[-1])

#wycinanie tekstu z całego tekstu
ss = "hello world"
print(ss[3:9])
#od elementu 2 do kóńca
print(ss[3:-1])
#od elementu  do kóńca
print(ss[3:])
#wycianie z krokiem 3
print(ss[::3])
#wycianie z krokiem 3 od 2 do 9
print(ss[2:9:3])

#liczenie wystąpień
txt = "abarakadabra"
n = txt.count("a")
print(n)

#dzielenie tekstu
a = "ala ma kota"
s= a.split(" ")
print(s)
# wyświetlenie calego z listy
print(s[2])
