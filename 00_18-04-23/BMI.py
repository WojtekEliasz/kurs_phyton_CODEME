
h = float(input("podaj swoj wzrost ->"))
w = float(input ("podaj swoja wage ->"))



BMI = (w / h ** 2)

print ("BMI wynosi", round (BMI, 2))


# to samo zamiana przecinka na kropkę


w = input("Podaj wagę ->")
h = input("Podaj wzrost ->")

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))

bmi = w / (h ** 2)
print("Your BMI is:", round(bmi, 2))


