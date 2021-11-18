MIN_LIKES = 500
MIN_SHARES = 100

like = 1000
shares = 50

if like > 500 and shares > 100:
    print("Mamy zniżkę 10%!!!")
elif like > 500 and shares < 100:
    print("Mamy już wystarczająco lajków:", like, "ale brakuje nam jeszcze:", MIN_SHARES-shares, "udostępnień")
elif like < 500 and shares > 100:
    print("Mamy już wystarczająco udostępnień:", shares, "ale brakuje nam jeszcze:", MIN_LIKES-like, "lajków")
else:
    print("Brakuje nam", MIN_LIKES-like,"lajków i", MIN_SHARES-shares, "udostępnień do uzyskania zniżki 10%")

print("\n\tZadanie 2).")
isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if isPizzaOrdered and isBigDrinkOrdered and not isWeekend:
    print("Gratulacje! Dostałeś kupon na burgera")
else:
    print("Zapraszamy do dalszych zakupów")

print("\n\tZadanie 3).")
diskSize = 140
diskSizeUsed = 133
fileSize = 20

if diskSize-diskSizeUsed >= fileSize:
    print("File can be downloaded")
else:
    print("Sorry. Disk is full")