string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for a in range(1,11):
    print(a, string_A)

for b in range(1,10):
    if b % 2 == 0:
        print(b, string_A)
    else:
        print(b, string_B)
    
for c in range(1,10):
    print( c * "x")
    
for d in range(1,10):
    if d % 2 == 0:
        print(d * "x")
    else:
        print(d * "o")
