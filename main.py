import random

numbers = list(range(1, 101))
secret_number = random.choice(numbers)

isFirtRun = True
chosen_number = 0

print("Welcome to Secret-Number!\n")

while chosen_number != secret_number and chosen_number != -1:
    try:
        if isFirtRun:
            chosen_number = int(
                input("Enter a number between 1 and 100 [-1 to exit].: "))
            isFirtRun = False
        else:
            chosen_number = int(
                input("Ups! That's was so close, try again [-1 to exit]: "))
    except ValueError:
        print("That's not a number, ha!")

if chosen_number == -1:
    print("You were defeated by your impatience. Good luck for next time!")
else:
    print("Perfect, yoy did it! Thanks to play!")
