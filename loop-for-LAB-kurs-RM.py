data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for y in data:
    print(y.upper())

print("\tZad 2)")

# for x in data:
#    elements = x.split()
#    print(elements)
#    print(elements[0].upper())
#    print(elements[1])


print("\tZad 3)")
for x in data:
    elements = x.split()
    if elements[0].find("Error"):
        print(elements[1].upper())
    else:
        print(elements[1])