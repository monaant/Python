# Zadanie 3
# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.


names_list = input("Podaj dowolną liczbę imion: ")
names_list1 = names_list.split(' ')
for user in range(999):
    print('Cześć', names_list1[user])

