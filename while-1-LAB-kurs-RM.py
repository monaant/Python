number = 1
previousNumber = 0


while number <= 50:
    print(previousNumber,"+", number, "=", previousNumber + number)
    previousNumber = number
    
    number+=1

print("\tZad2)")

import random
my_number = random.randint(0,20)

guess = -1

print("Guess my number!")
while guess != my_number:
    guess = int(input())
    if guess == my_number:
        print("Congratulation!")
    elif my_number < guess:
        print( "Sorry- my number is smaller than your guess, Try again!")
    else:
        print("Sorry- my number is greater than your guess, Try again!")