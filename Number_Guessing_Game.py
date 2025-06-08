import random   # Python's Built-In library random

# Generate a random number between 1 to 100
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 to 100. Now try to guess it!")

while True:
    # Take user input
    guess = int(input("Enter a guess number: "))

    # Check the guess
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} correctly!")
        break