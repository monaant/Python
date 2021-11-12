# Zadanie 5 – twierdzenie Pitagorasa
# Pamiętacie z matematyki twierdzenie Pitagorasa?
# Trójkąt pitagorejski, to trójkąt prostokątny, którego boki są wyrażone liczbami naturalnymi a, b, c związanymi warunkiem: a2+b2=c2.

# a) Poproś użytkownika o podanie długości boków A, B i C i sprawdź czy w ogóle możliwe jest utworzenie z nich trójkąta 🙂

# b) Odpowiedz czy trójkąt jest trójkątem pitagorejskim.

# c) Szczególnym przypadkiem jest trójkąt egipski o stosunkach długości 3:4:5. Sprawdź czy trójkąt pitagorejski jest trójkątem egipskim.

# d) Uwzględnij, że kolejność danych nie musi mieć znaczenia! Tzn. długość C użytkownik może podać jako pierwszą wartość. Przypomnij sobie zadanie 3 🙂

# Przykładowe dane:

# nie-trójkąty: [6, 9, 20], [3, 6, 11], [31, 14, 17]
# trójkąty nie-pitagorejskie: [4, 4, 4], [31, 17, 16], [10, 5, 8]
# trójkąty pitagorejskie: [3, 4, 5], [6, 8, 10], [5, 12, 13], [9, 40, 41], [8, 15, 17]
# trójkąty egipskie: [9, 12, 15], [3, 4, 5], [15, 20, 25], [6, 8, 10]

print("Sprawdzimy jaki trójkąt uda nam się zbudować :)")
a = int(input("Podaj długość jednego boku: "))
b = int(input("Podaj długość drugiego boku: "))
c = int(input("Podaj długość trzeciego boku: "))

if a == b == c or a > b > c or b > c > a or c > a > b:
    print("Możemy zbudować trójkąt")
if  a > b > c and a + b > c or b > c > a and b + c > a or c > a > b and c + a > b:
    print("Możemy zbudować trójkąt nie-pitagorejski")
elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2:
    print("To trójkąt pitagorejski")
    a1 = a / 3 
    b1 = b / 4
    c1 = c / 5
    if a1 == b1 == c1:
        print("To również szególny typ trójkąta pitagorejskiego - trójkąt egipski")
    else:
        print("Ale nie egipski")
else:
    print("Nie zbudujemy trójkąta")
 



