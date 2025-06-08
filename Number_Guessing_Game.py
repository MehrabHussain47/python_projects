import random

number = random.randint(1, 100)

print("Welcome to the number guessing game!")
print("You have to guess a number between 1 to 100. Now try to guess it!")

while True:
    guess = int(input("Enter a guess number: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guess the number {number} correctly!")
        break