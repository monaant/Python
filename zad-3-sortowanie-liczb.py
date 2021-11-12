# Zadanie 3 – sortowanie liczb
# Trzy dowolne liczby zapisz do trzech zmiennych.
# Znajdź największą liczbę.
# Wyświetl liczby od największej do najmniejszej.

x = 1
z = 46
y = 11

zmienne = x, z, y

if x < y and y < z:
    print("x < y < z czyli", x, "<", y, "<", z)
elif x > y and y > z:
    print("x > y > z czyli:", x, ">", y, ">", z)
elif x < z and z < y:
    print("x < z < y czyli:", x, "<", z, "<", y)
elif x > z and z > y:
    print("x > z > y czyli:", x, ">", z, ">", y)
else:
    print("coś nie tak...")

sortowanie = sorted(zmienne)
print(sortowanie)