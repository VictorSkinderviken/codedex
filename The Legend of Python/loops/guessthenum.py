import random

# Generate a random number once at the start (not in the loop)
random = random.randint(1, 9)
guess = 0
tries = 5

while guess != random and tries > 0:
    guess = int(input("Guess the number between 1-9: "))
    tries -= 1

    if guess != random and tries > 0:
        print(f"Wrong! Tries left: {tries}")
        
    elif guess != random and tries == 0:
        print(f"You're out of tries! The number was {random}.")

if guess == random:
    print("You got it!")