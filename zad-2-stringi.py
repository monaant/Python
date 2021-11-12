# Zadanie 2
# 1. Utwórz skrypt, który zapyta użytkownika o imię, nazwisko i numer telefonu, a następnie:

# 2. Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
# 3. Użytkownicy bywają leniwi. Nie zawsze zapisują imię czy nazwisko z dużej litery – popraw ich
# 4. Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
# 5. Zakładając, że twoi użytkownicy noszą polskie imiona, sprawdź czy użytkownik jest kobietą
# 6. Połącz dane w jeden ciąg personal za pomocą spacji
# 7. Policz liczbę wszystkich znaków w napisie personal
# 8. Podaj liczbę tylko liter w napisie personal
#  Podpowiedź – weź pod uwagę, że numery telefonów w Polsce są 9-cyfrowe

imie = input("Jak masz na imię? ")
nazwisko = input("Podaj proszę swoje nazwisko: ")
telefon = input("Podaj numer swój numer telefonu: ")

print("Ad2.")
print(imie.isalpha())
print(nazwisko.isalpha())
print(telefon.isdigit())
print("Ad3.")
imie1 = imie.title()
print(imie1)
nazwisko1 = nazwisko.title()
print(nazwisko1)
print("Ad4.")
telefon1 = telefon.replace(" ", "")
telefon2 = telefon1.replace("-", "")
print(telefon2)
print("Ad5.")
print(imie.endswith("a"))
print("Ad6.")
personal = imie1 + " " + nazwisko1 + " - telefon: " + telefon2
print(personal)
print("Ad7.")
print(len(personal))
print("Ad 8.")
lentelefon = len(personal) - len(telefon2)
print(lentelefon)

