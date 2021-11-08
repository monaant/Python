waga = input("Hej, Obliczę Twoje BMI. Ile ważysz w kg?")
wzrost = input("Ile masz wzrostu (podaj w metrach po kropce)?")

waga = float(waga)
wzrost = float(wzrost)
BMI = waga / (wzrost ** 2)

print("Twoje BMI wynosi: ", BMI)

if BMI < 15:
    print("Ważysz za mało")
elif 15.1 < BMI < 18.4:
    print("Masz niedowagę")
elif 18.5 < BMI < 24.9:
    print("Ważysz prawidołowo")
elif 25 < BMI < 29.9:
    print("Masz nadwagę")
elif 30 < BMI < 34.9:
    print("I stopień otyłości")
elif 35 < BMI < 39.9:
    print("Drugi stopień otyłości")
else:
    print("III stopień otyłości (Otyłość skrajna)")