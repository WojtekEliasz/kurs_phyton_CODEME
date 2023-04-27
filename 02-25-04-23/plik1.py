# sprawdzanie czy ciąg znaków składa się z cyfr



print("1234".isnumeric())

"1234".isdigit()

#print(”mata”.center(10, '*'))

print("lalalaaaaaa".rstrip('a'))


print("www.flynerd.pl".removeprefix('w'))

print("atagatataaaaa".rstrip("ta")) # Rstrip =- z prawej

print("atagatataaaaa".strip("ta"))

print("banana".count('na'))


# palindrom
#Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

palindrom = input("podaj tekst:")
palindrom = palindrom.replace(" ","").upper()
print("czy to palndrom", (palindrom == palindrom[::-1]))

