numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
max = len(numbers)-1

while i < max:
    print(i, numbers[i], numbers[i+1])
    if numbers[i]**2 == numbers[i+1]:
        print("\tFaund: ", numbers[i], numbers[i+1])
    i += 1

print("\tZad2)")

numbers1 = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]

i = 0
max = len(numbers1)-2
while i < max:
    print(i, numbers1[i], numbers1[i+1], numbers1[i+2])
    if numbers1[i]**2 == numbers1[i+1] and numbers1[i+1]**2 == numbers1[i+2]:
        print("\tFaund: ", numbers1[i], numbers1[i+1], numbers1[i+2])
    i += 1

print("\tZad3)")

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

t1 = 0
tmax = len(texts)-1
while t1 < tmax:
    print(t1, texts[t1], texts[t1+1])
    if len(texts[t1]) == len(texts[t1+1]):
       print("\tFaund: ", texts[t1], "=", len(texts[t1]), texts[t1+1], "=", len(texts[t1+1]))

    t1 += 1

