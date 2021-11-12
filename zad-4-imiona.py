# Zadanie 4 – imiona
# Utwórz zbiór imion męskich i żeńskich. Poproś użytkownika o podanie imienia. Sprawdź czy imię jest męskie czy żeńskie i wyświetl na ten temat informację. Jeżeli imienia nie ma na liście wyświetl komunikat „Nie znamy tego imienia.” Następnie użytkownik poda informację czy imię jest męskie czy żeńskie. Dodaj imię do listy.

imiona = {"Anna":"żeńskie", "Błażej":"męskie", "Krzysztof":"męskie", "Marta":"żeńskie", "Monika":"żeńskie", "Maciej":"męskie", "Katarzyna":"żeńskie", "Mikołaj":"męskie", "Adrian":"męskie"}
imie = input("Jak masz na imię? ")

imie1 = imie[-1]
if imie1 == "a":
    print("Jesteś kobietą!")
else:
    print("Jesteś mężczyzną!")

if imie in imiona:
    print("Jesteś na liście")
elif imie not in imiona:
    print("Nie znamy tego imienia")
    nowe = input("Czy chcesz dodać nowe imię? (t/n) ")
    if nowe == "t":
        płeć = input("Czy to żeńskie imię? (t/n) ")
        if płeć =="t":
            imiona[imie] = "żeńskie"
            for im, pł in imiona.items():
                print(im + " to imię " + pł)
        else:
            imiona[imie] = "męskie"
            for im, pł in imiona.items():
                print(im + " to imię " + pł)
else:
    print("Ok")




