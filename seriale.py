# Zadanie 2
# Utwórz spis oglądanych seriali.
# Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
# Zapytaj użytkownika jaki serial chce obejrzeć.
# W odpowiedzi podaj jego ocenę.
# Zapytaj użytkownika o dodanie kolejnego serialu i oceny.
# Dodaj serial do spisu.

seriale = {"Arkane":2, "Dexter":5, "Stranger Things":10, "Gra o Tron":10, "The Walking Dead":8, "Wikingowie":7}

print("Co chciałbyś obejrzeć? ")
for serial in seriale:
    print(serial)
print("-" * 40)
serial = input("Podaj proszę nazwę serialu ")
print("-" * 40)
print(serial, "ma ocenę", seriale[serial])
print("-" * 40)
nowy = input("Czy chciałbyś dodać serial i ocenę? (tak/nie) ")
if nowy == 'tak':
    serial_nowy = input("Podaj proszę nazwę: ") 
    ocena_nowa = input("Podaj proszę ocenę: ")
    seriale[serial_nowy] = ocena_nowa
    print("-" * 40)
    for serial,ocena in seriale.items():
        print(serial, "ma ocenę", ocena)
else:
    print("ok")



