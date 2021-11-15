# Zadanie 4
# Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
# – czy liczba jest wielokrotnością 3
# – czy liczba jest wielkorotnością 4
# – wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
# – wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony

liczba = int(input("Podaj proszę liczbę: "))

if liczba % 3 == 0 and liczba % 4 != 0:
    print("Liczba jest wielokrotnością 3 ")
elif liczba % 3 != 0 and liczba % 4 == 0:
    print("Liczba jest wielokrotnością 4 ")
elif liczba % 3 == 0 and liczba % 4 == 0:
    print("Hurra ")
else:
    print("*")