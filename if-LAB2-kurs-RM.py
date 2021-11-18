musclePain = False
fever = True
weakness = True

if musclePain and fever and weakness:
    print("suspicion of influenza")
else:
    print("The flu is unlikely")

print("\t-----------")
if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and not (fever and musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")

print("\t-----------")
isMan = True

if musclePain and fever and weakness or isMan:
     print("suspicion of influenza")
elif weakness and not (fever and musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")


print("\t Zad2)")
isCheckCompleted = False

print("CHECK IS COMPLETED" if isCheckCompleted else "CHECK NOT DONE YET!")