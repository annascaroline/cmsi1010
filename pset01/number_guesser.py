
import random
secret = random.randint(1,1000)

attempts = 0
while True:
    guess = input("Guess the secret number or say 'bye' or 'exit' to exit.\n").strip().lower()
    if guess == 'bye' or guess == 'exit':
        print("Thanks for playing!")
        break
# Digit check
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    attempts = attempts + 1
    number = int(guess)
    if number > secret:
        print("Too high!")
    if number < secret:
        print("Too low!")
    if number == secret:
        print("Congratulations! You guessed the number!\nYou took", attempts, "tries.")
# Reseting lines
        secret = random.randint(1,1000)
        attempts = 0


