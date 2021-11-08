# Zadanie 2 – lokata
# Napisz skrypt, który, który obliczy stan konta za kilka lat. Program pyta użytkownika o:

# stan początkowy konta,
# stopę oprocentowania rocznego (zwróć uwagę, że odsetki podlegają miesięcznej kapitalizacji)
# liczbę lat na lokacie.
# Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu. Wypisz np. takie zdanie:
# Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
szer = 80

konto = int(input("Podaj początkowy stan konta: "))
oprocentowanie = int(input("Jakie jest oprocentowanie roczne? "))
czas = int(input("Ile lat będziesz trzymać środki? "))
wynik = (((konto * (oprocentowanie / 100)) * czas) + konto)
wynik = float(wynik)

print("-" * szer)
print("Twoje ", konto, "przez", czas, " lata, przy oprocentowaniu rocznym", oprocentowanie, "%", "urośnie do", wynik)
podatek = (wynik - konto) * 0.19
wynik2 = wynik - podatek
szer = 80
print("-" * szer)
print("Musisz jeszcze wziąć pod uwagę podatek Belki 19% czyli Twój realny zysk to będzie:", wynik2)