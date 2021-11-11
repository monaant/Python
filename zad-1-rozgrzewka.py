# Policz wszystkie znaki w napisie
# Nie modyfikując zmiennej sentence wyświetl słowo „prosty”
# Wyświetl znak o indeksie (czy za każdym razem rozumiesz co się dzieje?):
# 7
# 12
# -4
# 37
# Wprowadź do zdania 2 błędy ortograficzne 😉

sentence = "Kurs Pythona jest prosty i przyjemny."

print("Ad1)")
print(len(sentence))
print("Ad2)")
print(sentence[18:24])
print("Ad3)")
print(sentence[7])
print(sentence[12])
print(sentence[-4])

print("ad3)")
sentence = sentence[0:6] + "i" + sentence[7:20] + "ó" + sentence[21:]
print(sentence)
