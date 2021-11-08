# Praca siedząca, brak dodatkowej aktywności fizycznej	1,2
# Praca niefizyczna, mało aktywny tryb życia	1,4
# Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu	1,6
# Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu	1,8
# Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu	2,0

# Oblicz z pomocą pythona zapotrzebowanie kaloryczne:

# a) dla 25-letniej kobiety o wzroście 1.7m i wadze 63kg, która uprawia sport kilka razy w tygodniu.
# b) siebie samej / samego.
# Jeśli nie chce Ci się czytać wpisu to podaję wzory poniżej:

# Podstawa: 10 x masa ciała + 6.25 x wzrost w cm – 5 x wiek + S
# współczynnik S: dla kobiet = -161, dla mężczyzn= +5

print("Hej, Obliczę obliczę ile kalorii dziennie musisz jeść. ")
plec = input("Jesteś kobietą (K) czy mężczyzną? (M) ")
plec = plec.capitalize()
wiek = float(input("Ile masz lat? "))
waga = float(input("Ile ważysz? Podaj w kg "))
wzrost = float(input("Ile masz wzrostu? Podaj w cm "))
praca = input("Jaki tryb pracy wykonujesz? Podaj numerek abym mógł obliczyć:\n Praca siedząca, brak dodatkowej aktywności fizycznej - 1\n Praca niefizyczna, mało aktywny tryb życia - 2 \n Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu - 3\n Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu - 4\n Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu - 5\n   ")

kcalk = 10 * waga + 6.25 * wzrost - 5 * wiek - 161
kcalm = 10 * waga + 6.25 * wzrost - 5 * wiek + 5
if plec == 'K':
    print("Twoje zapotrzebowanie kaloryczne wynosi: ", kcalk)
elif plec == 'M':
    print("Twoje zapotrzebowanie kaloryczne wynosi: ", kcalm)
else:
    print("Ho ho ho coś jest źle")

if praca == '1':
    print("Biorąc pod uwagę tryb pracy i płeć Twoje zapotrzebowanie kcal wynosi: ", kcalm * 1.2 or kcalk * 1.2 )
elif praca == '2':
    print("Biorąc pod uwagę tryb pracy i płeć Twoje zapotrzebowanie kcal wynosi: ", kcalm * 1.4 or kcalk * 1.4 )
elif praca == '3':
    print("Biorąc pod uwagę tryb pracy i płeć Twoje zapotrzebowanie kcal wynosi: ", kcalm * 1.6 or kcalk * 1.6 )
elif praca == '4':
    print("Biorąc pod uwagę tryb pracy i płeć Twoje zapotrzebowanie kcal wynosi: ", kcalm * 1.8 or kcalk * 1.8 )
elif praca == '5':
    print("Biorąc pod uwagę tryb pracy i płeć Twoje zapotrzebowanie kcal wynosi: ", kcalm * 2 or kcalk * 2 )
else:
    print("Ho ho ho coś poszło nie tak...")
