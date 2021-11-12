print("Ile masz lat?")
age = int(input())
if age > 100:
    print ("Żyj nam 200 lat!")
elif age >= 18:
    print("Użytkownik pełnoletni")
else:
    print("Użytkowniku do pełnoletności zostało Ci:", (18 - age), "lat")