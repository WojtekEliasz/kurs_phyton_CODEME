# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. Załóżmy,
# że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
# Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.


spalanie_100km = input("podaj średnie spalanie pojazdu w l na 100km :")
spalanie_100km = float(spalanie_100km.replace(",", "."))

cena_l = input("podaj cenę paliwa za 1l w PLN:")
cena_l = float(cena_l.replace(",", "."))

dystans = int(input("podaj pokonany dystans w km:"))

koszt = (spalanie_100km * (dystans / 100) * cena_l)

print()
print("twój koszt przejazdu", dystans, "km to", round(koszt, 2), "PLN")

